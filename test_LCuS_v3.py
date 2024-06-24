import os
import numpy as np


"""
Naive implementation of LCuS that tests definitions from 6/24
"""


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
def gen_D(T, j, m):
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
def LCuS(s, ideal, j, m):
  n = len(s)
  empty_T = np.zeros((n+1, n+1, n+1, n+1, n+1), dtype=int)
  # populate values of tensor T
  T = populate_T(empty_T, s)
  # extracts the largest tuple (p, q) s.t. T[n][p][p+1][q][q+1] is maximized
  p, q = find_pq(T, n)[-1]

  # select ideal j, l, m parameters
  if ideal:
    j = (int)(p+1)
  # otherwise takes user-inputted parameters
  
  # generate f, d, and e two-dimensional matrices for fixed j, l, m
  params = (T, j, m)
  F = gen_F(*params) 
  D = gen_D(*params)
  A = gen_A(D, j, m)
  # print(A)

  # write to file named after j, l, m params and stored in folder named after string
  file_name = str(f"results_v2/{s}/{j}_{m}.txt")
  # folder is named after the string
  os.makedirs(os.path.dirname(file_name), exist_ok=True)
  file = open(file_name, "w")
  # display string and i, j, k, l, m parameters
  file.write(f"s = {s}\n\n")
  file.write(f"j = {j}\n")
  file.write(f"m = {m}\n\n")

  file.write(f"i is in range [1, {j})\n")
  file.write(f"k is in range [{j}, l)\n")
  file.write(f"l is in range [2, {m})\n\n")

  # display the substrings that would result from the split from the j, l, m values
  # file.write(f"substrings: {s[0:j-1]}, {s[j-1:l-1]}, {s[l-1:m]}\n\n")
  # indicate the values of p and q if ideal parameters are requested
  file.write(f"\tp = {p}, q = {q}\n\n")

  eq_signs = (m+5) * "="
  file.write(f"{eq_signs} A {eq_signs}\n")
  file.write(str(A))

  # format and print the f, d  matrices (for specified j, l, m values)
  file.write(f"\n\n{eq_signs} F, D {eq_signs}\n")
  
  for x in range(len(F)):
    dashes = (m+2) * "-"
    file.write(f"\n{dashes} l = {x+2} {dashes}\n")
    file.write(str(F[x]) + '\n\n' + str(D[x])+ '\n\n')
  
  file.close()
  
  # inform the user of the name of their file
  print(f"\nYour file was saved: {file_name}\n")

'''
# Prompts user for an integer in the range (lower, upper) with exclusive bounds
# until a valid integer is entered and returns this valid integer. 
'''
def check_input(str_x, lower, upper):
  validInput = False
  while not validInput:
    try:
      x = int(input(f"{str_x}: "))
      if x > lower and x < upper:
        validInput = True
      else:
        print(f"Enter an integer in the proper range: {lower} < {str_x} < {upper}.")
    except ValueError:
      print("Enter a positive integer.")
  return x

############################################################################################
# Interactive portion of the program
############################################################################################

s = input("\nEnter string: ")
ideal = True if input("\nUse ideal j? (Yes/No): ").lower() == 'yes' else False

# case where user wants to select j, l, m parameters
  # ensure that valid inputs are entered for j, l, m
if not ideal:
  print(f"\nEnter positive integers 2 <= j < m <= {len(s)}.")
  j = check_input("j", 1, len(s))
else:
  j = 0
  # l = check_input("l", j, len(s) + 1)
print(f"\nEnter positive integer {j} < m <= {len(s)}.")
m = check_input("m", j, len(s) + 1)
# otherwise user wants to use ideal parameters


# write parameters and matrices to a text file
LCuS(s, ideal, j, m)
