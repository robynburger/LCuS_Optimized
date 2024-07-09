# Testing out reccurence relations for h 

import numpy as np
import sys
import random

# gamma(m, x, seq) is the largest value of r such that r <= x and 
# seq[r] == seq[m], or 0 if no such value exists
def gamma(m, x, seq):
    for r in range(x, 0, -1):
        if seq[r-1] == seq[m-1]:
            return r
    return 0

def test(seq):

    n = len(seq)
    f = np.zeros((n+1, n+1, n+1, n+1, n+1), dtype=int)      # f[m,j,i,k,l]
    A = np.zeros((n+1, n+1, n+1, n+1), dtype=int)

    for m in range(1, n+1):
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                for k in range(j, n+1):
                    for l in range(k+1, m+1):
                        f[m, i, j, k, l] = f[m-1, i, j, k, l]
                        if gamma(m, i, seq) > 0 and gamma(m, k, seq) >= j:
                            f[m, i, j, k, l] = max(f[m, i, j, k, l], 
                                                   f[m-1, gamma(m, i, seq)-1, j, gamma(m, k, seq)-1, l]+1)
                            if f[m, i, j, k, l] > f[m, i-1, j, k, l]:
                                A[m, i, k, l] = j

    # a[m, i, k, l]
    a = np.zeros((n+1, n+1, n+1, n+1), dtype=int)
    # h[m, i, k, l]
    h = np.zeros((n+1, n+1, n+1, n+1), dtype=int)
    for m in range(1, len(seq)+1):
        for l in range(1, m):
            # compute h
            for k in range(1, l):
                for i in range(1, k):
                    maximum = a[m-1, i-1, k, l]
                    if gamma(m, i-1, seq) < i-1:
                        maximum = max(maximum, h[m, i-1, k, l])
                    if gamma(m, k-1, seq) < k-1:
                        maximum = max(maximum, h[m, i, k-1, l])
                    h[m, i, k, l] = maximum
                    if h[m, i, k, l] > 0:
                        print(f"h[{m}, {i}, {k}, {l}] = {h[m, i, k, l]}")
            
            # compute a
            for k in range(1, l):
                for i in range(1, k):
                    if gamma(m, i-1, seq) < 1 or gamma(m, k-1, seq) <= i:
                        a[m, i, k, l] = a[m-1, i, k, l]
                    else:
                        a[m, i, k, l] = min(a[m-1, i, k, l], h[m, i, k, l])
                    if seq[i-1] == seq[k-1] == seq[m-1]:
                        if gamma(m, i-1, seq) < 1 or gamma(m, k-1, seq) <= i:
                            a[m, i, k, l] = m
                        else:
                            a[m, i, k, l] = h[m, i, k, l]
                    elif seq[i-1] == seq[m-1]:
                        if gamma(m, k-1, seq) >= i+1:
                            a[m, i, k, l] = max(a[m, i, k, l], a[m, i, gamma(m, k-1, seq), l])
                    elif seq[k-1] == seq[m-1]:
                        if gamma(m, i-1, seq) >= 1:
                            a[m, i, k, l] = max(a[m, i, k, l], a[m, gamma(m, i-1, seq), k, l])
                    
                    print(f"a[{m}, {i}, {k}, {l}] = {a[m, i, k, l]}")
                    if a[m, i, k, l] != A[m, i, k, l]:
                        print(f"  error, should be {A[m, i, k, l]}");
                        print(f"  s_i = {seq[i - 1]}, s_k = {seq[k - 1]}, s_m = {seq[m - 1]}");
                        print(f"  gamma(m, i-1) = {gamma(m, i-1, seq)}");
                        print(f"  gamma(m, k-1) = {gamma(m, k-1, seq)}");
                        break


seq = "aabdaibxbabb"
test(seq)

def h(i, k, l, m, seq):
  if gamma(k, i-1, seq) == 0 or gamma(k, m-1, seq) == 0:
      return k
  max = 0
  for r in range(gamma(k, i-1, i)):
      for s in range(gamma(k, m-1, m)): 
          temp = a(r, k-1, l, s) 
          if temp > max:
            max = temp
  return max

def a(i, k, l, m, seq): 
    if seq[i-1] == seq[k-1] == seq[m-1]:
        return h(i, k, l, m, seq)
    return min(a(i, k-1, l, m), h(i, k, l, m))