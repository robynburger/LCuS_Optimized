import os
import numpy as np
import naive as n_file
import LCuS_v3 as t_file
import random 

"""
Tests t_file against n_file, using randomly generated string made of letters 
from alphabet

to test one string, set num_tests = 1 and set seq equal to the sequence
"""

# characters allowed in test string 
alphabet = ['a', 'b', 'c', 'd']

# max size of the test string 
max_length = 10

# true if you want all error messages, false if you don't (better for more test cases)
verbose = True 

# number of test cases
num_tests = 1

def test_verbose(seq):
  naive_A = n_file.naive(seq)
  test_A = t_file.optimized(seq)
  n = len(seq)
  # print(f"\nTesting {seq}\n")
  for m in range(1, n+1):
    for j in range(1, m):
      # compute h
      for i in range(1, j):
        for k in range(j, m):
          if naive_A[m, j, i, k] != test_A[m, j, i, k]:
                  print(f"\n \t error: {seq}, A[{m}, {j}, {i}, {k}] = {test_A[m, j, i, k]} but should be {naive_A[m, j, i, k]}\n")
                  print(f"    s_i = {seq[i-1]}, s_k = {seq[k-1]}, s_m = {seq[m-1]}")
                  print(f"    gamma(m, i-1) = {n_file.gamma(m, i-1, seq)}");
                  print(f"    gamma(m, k-1) = {n_file.gamma(m, k-1, seq)}");
  print(f"Test done: {seq}")

def test_concise(seq):
  skip = False
  naive_A = n_file.naive(seq)
  test_A = t_file.optimized(seq)
  n = len(seq)
  # print(f"\nTesting {seq}")
  for m in range(1, n+1):
    for j in range(1, m):
      # compute h
        for i in range(1, j):
          if skip == False:
            for k in range(j, m):
              if skip == False:
                if naive_A[m, j, i, k] != test_A[m, j, i, k]:
                  skip = True
                  print(f"\nFailed: {seq}, A[{m}, {j}, {i}, {k}] = {test_A[m, j, i, k]} but should be {naive_A[m, j, i, k]}\n")
                  print(f"    s_i = {seq[i-1]}, s_k = {seq[k-1]}, s_m = {seq[m-1]}")
                  print(f"    gamma(m, i-1) = {n_file.gamma(m, i-1, seq)}");
                  print(f"    gamma(m, k-1) = {n_file.gamma(m, k-1, seq)}\n");
  
  # if skip == False: 
  #    print(f"\nPassed: {seq}\n")


for _ in range(num_tests):
  seq = ""
  for _ in range(random.randint(3, max_length)):
    seq += str(random.choice(alphabet))

  if verbose:
    test_verbose(seq)
  else: 
    test_concise(seq)
