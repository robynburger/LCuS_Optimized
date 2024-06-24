## File that will hold new algorithm with modified outputs 

import numpy as np

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
    A = np.zeros((n+1, n+1, n+1, n+1), dtype=int)      # A[m,j,i,k]
    for m in range(1, n+1):
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                for k in range(j, n+1):
                    for l in range(k+1, m+1):
                        f[m,j,i,k,l] = f[m - 1,j,i,k,l]
                        if gamma(m,i,seq) > 0 and gamma(m,k,seq) >= j:
                            f[m,j,i,k,l] = max(f[m,j,i,k,l], f[m-1,j,gamma(m,i,seq)-1, gamma(m,k,seq)-1,l]+1)
                        if f[m,j,i,k,l] > f[m,j,i-1,k-1,l] and seq[i-1] == seq[k-1]:
                            A[m,j,i,k] = l
                            print(f"d[{m}, {j}, {i}, {k}, {l}] = 1")
                    if A[m,j,i,k] > 0:
                        print(f"A[{m}, {j}, {i}, {k}] = {A[m,j,i,k]}")
    
    # O(n^4) implementation below
    h = np.zeros((n+1, n+1, n+1, n+1), dtype=int)   # h[m,j,i,k]
    a = np.zeros((n+1, n+1, n+1, n+1), dtype=int)   # a[m,j,i,k]
    for m in range(1, n+1):
        for j in range(1, m):
            # compute h
            for i in range(1, j):
                for k in range(j, m):
                    if (i-1 < 1 and k-1 < j) or (gamma(m,i-1,seq) < 1 and gamma(m,k-1,seq) < j):
                        h[m, j, i,k] = m
                    else:
                        if (i-1 < 1) or (k-1 < j) or (gamma(m,i-1,seq) < 1) or (gamma(m,k-1,seq) < j):
                            h[m, j, i,k] = 0
                        else:
                            maximum = a[m-1,j,i-1,k-1]
                            if gamma(m,i-1,seq) < i-1:
                                maximum = max(maximum, h[m, j, i-1, k])
                            if gamma(m,k-1,seq) < k-1:
                                maximum = max(maximum, h[m, j, i, k-1])
                            h[m,j,i,k] = maximum
                            if h[m,j,i,k] > 0:
                                print(f"h[{m}, {j}, {i}, {k}] = {h[m, j, i, k]}")

            # compute a
            # not checking if a_m-1^j(i, k) is properly defined b/c 
            # m starts at 1 and m = 0 is defined in tensor as 0 
            for i in range(1, j):
                for k in range(j, m):
                    if seq[i-1] == seq[k-1] == seq[m-1]:
                      a[m, j, i, k] = h[m, j, i, k]
                    elif seq[i-1] == seq[k-1]:
                      a[m, j, i, k] = min(a[m-1, j, i, k], h[m, j, i, k])
                    else: 
                      a[m, j, i, k] = 0
                    if a[m, j, i, k] > 0:
                       print(f"a[{m}, {j}, {i}, {k}] = {a[m, j, i, k]}")

                    

test("abcadbabcabyc")

