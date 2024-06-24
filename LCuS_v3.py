## inspired by Adiesha's new definition from 6/24
# File that will hold new algorithm with modified outputs 

import numpy as np

# gamma(m, x, seq) is the largest value of r such that r <= x and 
# seq[r] == seq[m], or 0 if no such value exists
def gamma(m, x, seq):
    for r in range(x, 0, -1):
        if seq[r-1] == seq[m-1]:
            return r
    return 0

# O(n^4) implementation
def optimized(seq):
    n = len(seq)
    h = np.zeros((n+1, n+1, n+1, n+1), dtype=int)   # h[m,j,i,k]
    a = np.zeros((n+1, n+1, n+1, n+1), dtype=int)   # a[m,j,i,k]
    for m in range(1, n+1):
        for j in range(1, m):
            # compute h
            for i in range(1, j):
                for k in range(j, m):
                    if (i-1 < 1 and k-1 < j) or (gamma(m,i-1,seq) < 1 and gamma(m,k-1,seq) < j):
                        h[m, j, i, k] = m
                    else:
                        if (i-1 < 1) or (k-1 < j) or (gamma(m, i-1, seq) < 1) or (gamma(m, k-1, seq) < j):
                            h[m, j, i, k] = m
                        else:
                            maximum = a[m-1, j, i-1, k-1]
                            if gamma(m, i-1, seq) < i-1:
                                maximum = max(maximum, h[m, j, i-1, k])
                            if gamma(m, k-1, seq) < k-1:
                                maximum = max(maximum, h[m, j, i, k-1])
                            h[m, j, i, k] = maximum
                            #if h[m,j,i,k] > 0:
                                #print(f"h[{m}, {j}, {i}, {k}] = {h[m, j, i, k]}")

            # compute a
            # not checking if a_m-1^j(i, k) is properly defined b/c 
            # m starts at 1 and m = 0 is defined in tensor as 0 
            for i in range(1, j):
                for k in range(j, m):
                    if seq[i-1] == seq[k-1] == seq[m-1]:
                      a[m, j, i, k] = h[m, j, i, k]
                    elif seq[i-1] == seq[k-1]:
                    #   print("si = sk")
                      a[m, j, i, k] = min(a[m-1, j, i, k], h[m, j, i, k])
                    #   print(f"a[{m-1}, {j}, {i}, {k}] = {a[m-1, j, i, k]}")
                    #   print(f"h[{m}, {j}, {i}, {k}] = {h[m, j, i, k]}")
                    else: 
                      a[m, j, i, k] = 0
    return a           


