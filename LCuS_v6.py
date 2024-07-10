"""
Testing possible recurrence relations for h and a functions. 
Using an alternative definition of d: f(m, i, j, k, l) - f(m, i, j, k-1, l)
so that we are varying the last segment instead of the second segment. 
The a function should give us some value of l. The l's are contiguous and start at k+1. 
"""
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
    f = np.zeros((n+1, n+1, n+1, n+1, n+1), dtype=int)      # f[m, i, j, k, l]
    A = np.zeros((n+1, n+1, n+1, n+1), dtype=int)           # A[m, i, j, k]

    for m in range(1, n+1):
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                for k in range(j, n+1):
                    for l in range(k+1, m+1):
                        f[m, i, j, k, l] = f[m-1, i, j, k, l]
                        if gamma(m, i, seq) > 0 and gamma(m, k, seq) >= j:
                            f[m, i, j, k, l] = max(f[m, i, j, k, l], 
                                                   f[m-1, gamma(m, i, seq)-1, j, gamma(m, k, seq)-1, l]+1)
                        if f[m, i, j, k, l] > f[m, i, j, k-1, l]:
                            A[m, i, j, k] = l

    # a[m, i, j, k]
    a = np.zeros((n+1, n+1, n+1, n+1), dtype=int)
    # h[m, i, j, k]
    h = np.zeros((n+1, n+1, n+1, n+1), dtype=int)
    
    for m in range(1, n+1):
        for j in range(1, m):
            # compute h
            for i in range(1, j):
                for k in range(j, m):
                    maximum = a[m-1, i-1, j, k-1]
                    if gamma(m, i-1, seq) < i-1:
                        maximum = max(maximum, h[m, i-1, j, k])
                    if gamma(m, m-1, seq) < k-1:
                        maximum = max(maximum, h[m, i, j, k-1])
                    h[m, i, j, k] = maximum
                    # if h[m, i, k, l] > 0:
                        # print(f"h[{m}, {i}, {k}, {l}] = {h[m, i, k, l]}")
    
            # compute a
            for i in range(1, j):
                for k in range(j, m):
                    if seq[k-1] == seq[m-1] and seq[i-1] != seq[m-1] and gamma(m, i-1, seq) >= 1:
                        a[m, i, j, k] = a[m, gamma(m, i-1, seq), j, k]
                    elif seq[i-1] == seq[m-1] and seq[i-1] != seq[m-1] and gamma(m, k-1, seq) >= j:
                        a[m, i, j, k] = a[m-1, i, j, k]
                    elif seq[i-1] == seq[k-1] == seq[m-1]:
                        if gamma(m, i-1, seq) < 1 or gamma(m, k-1, seq) < j:
                            a[m, i, j, k] = m
                        else:
                            a[m, i, j, k] = h[m, i, j, k]
                    elif gamma(m, i-1, seq) < 1 or gamma(m, k-1, seq) < j:
                        a[m, i, j, k] = a[m-1, i, j, k]
                    else:
                        a[m, i, j, k] = min(a[m-1, i, j, k], h[m, i, j, k])
                    
                    print(f"a[{m}, {i}, {j}, {k}] = {a[m, i, j, k]}")
                    if a[m, i, j, k] != A[m, i, j, k]:
                        print(f"  error, should be {A[m, i, j, k]}")
                        # print(f"  s_i = {seq[i - 1]}, s_k = {seq[k - 1]}, s_m = {seq[m - 1]}")
                        # print(f"  gamma(m, i-1) = {gamma(m, i-1, seq)}")
                        # print(f"  gamma(m, k-1) = {gamma(m, k-1, seq)}")


seq = "babbcaba"
test(seq)