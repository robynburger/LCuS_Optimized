import os
import numpy as np
import LCuS_v3 as test_file
import random 

"""
Tests 
"""

alphabet = ['a', 'b', 'c', 'd', 'x', 'y']
seq = ""
for _ in range(random.randint(3, 30)):
  seq += str(random.choice(alphabet))

naive_A = test_file.naive(seq)
optimized_A = test_file.optimized(seq)


'''
# Populates the tensor T such that T[m][i][j][k][l] = f_m(i, j, k, l) 
# for all valid inputs and returns the populated tensor.
'''
def populate_T(T, s):
  n = len(s)
  for m in range(1, n+1):
    for i in range (1, m+1): 
      for j in range(i+1, m+1):
        for k in range(j, m+1): 
          for l in range(k+1, m+1):
            if s[i-1] == s[k-1] == s[m-1]: 
              T[m][i][j][k][l] = T[m-1][i-1][j][k-1][l] + 1 
            else:
              T[m][i][j][k][l]= max(T[m][i-1][j][k][l], 
                                    T[m][i][j][k-1][l], 
                                    T[m-1][i][j][k][l])
  return T

'''
# Returns a list of tuples (p, q) such that T[n][p][p+1][q][q+1] 
# is maximized.
'''
def find_pq(T, n):
  # keys are ints (values of T), values are lists of tuples
  d = dict()
  for i in range(1, n):
    for k in range(i+1, n):
      if T[n][i][i+1][k][k+1] in d.keys():
        d[T[n][i][i+1][k][k+1]].append((i, k))
      else:
        d[T[n][i][i+1][k][k+1]] = [(i, k)]

  max_f = max(d.keys())
  # return dict value (list of tuples) corresponding to max key (T-value)
  return d[max_f]

'''
# Generates the f matrix for fixed values of m, j, l.
# Note: the leftmost column and top row correspond to i=0 and k=0, respectively, 
# so the leftmost column and top row will always consist entirely of 0s.
'''
def gen_F(T, j, m):
  F_list = []
  for l in range(2, m+1):
    F = np.zeros((j, l), dtype=int) 
    for i in range(1, j):
      for k in range (j, l):
        F[i, k] = T[m][i][j][k][l]
    F_list.append(F)
  return F_list

'''
# Generates the d matrix for fixed values of m, j
# Note: the leftmost column and top row correspond to i=0 and k=0, respectively, 
# so the leftmost column and top row will always consist entirely of 0s.
'''
def gen_D(T, j, m, s):
  F_list = gen_F(T, j, m)
  D_list = []
  for l in range(2, m+1):
    D = np.zeros((j, l), dtype=int)
    for i in range(1, j):
      for k in range(j, l):
        if s[i-1] == s[k-1] and (F_list[l-2])[i, k] - (F_list[l-2])[i-1, k-1] == 1: 
          D[i, k] = 1
        else:
          D[i, k] = 0
    D_list.append(D)
  return D_list


'''
# Generates a_m^j(i,k), which is the max l such that d_m^j(i, k, l) = 1
'''
def gen_A(D_list, j, m):
  A = np.zeros((m+1, m+1), dtype=int) + 100 # high value meant to never be min
  # for elem in D_list: # indices range from 0 to m-2 inclusive - D[0] is l = 2
  for i in range(1, j):
    for k in range(j, m):
      max_l = 0
      for x in range(k+1, m+1):
        # print(f"i: {i}, k: {k}, x: {x-2}")
        # print(D_list[x-2][i, k])
        if D_list[x-2][i, k] == 1:
          max_l = x
      A[i, k] = max_l
  return A
  
'''
# Writes given parameters and f, d, e matrices to a text file which is stored in 
# a folder named after the given string and which has a file name consisting of 
# the j, l, m parameters. 
'''
def LCuS(s):
  n = len(s)
  empty_T = np.zeros((n+1, n+1, n+1, n+1, n+1), dtype=int)
  # populate values of tensor T
  T = populate_T(empty_T, s)
  # extracts the largest tuple (p, q) s.t. T[n][p][p+1][q][q+1] is maximized
  # p, q = find_pq(T, n)[-1]

  print(f"\nTESTING {seq}\n")
  
  for m in range(1, n+1):
    for j in range(1, m):
      params = (T, j, m, s)
      D = gen_D(*params)
      A = gen_A(D, j, m)
      for i in range (1, j): 
        for k in range(j, m): 
          if test_A[m, j, i, k] != A[i, k]:
            print(f"error, should be {A[i, k]}")
          # else:
          #   print(f"A[{m}, {j}, {i}, {k}] = {test_A[m,j,i,k]}")

  print("\nDONE\n")

# write parameters and matrices to a text file
# LCuS(seq)

LCuS(seq)
