# inspired by bmumey
import numpy as np

seq = "aabdaibxbabb"

def gamma(m, x):
    for r in range(x, 0, -1):
        if seq[r-1] == seq[m-1]:
            return r
    return 0

def test():
    # a[m, j, i, k]
    a = np.zeros((len(seq) + 1, len(seq) + 1, len(seq) + 1, len(seq) + 1), dtype=int)
    # h[m, j, i, k]
    h = np.zeros((len(seq) + 1, len(seq) + 1, len(seq) + 1, len(seq) + 1), dtype=int)
    for m in range(1, len(seq)+1):
        for j in range(1, m):
            # compute h
            for i in range(1, j):
                for k in range(j, m):
                    maximum = a[m-1, j, i-1, k-1]
                    if gamma(m, i-1) < i-1:
                        maximum = max(maximum, h[m, j, i-1, k])
                    if gamma(m, k-1) < k-1:
                        maximum = max(maximum, h[m, j, i, k-1])
                    h[m, j, i, k] = maximum
                    if h[m, j, i, k] > 0:
                        print(f"h[{m}, {j}, {i}, {k}] = {h[m, j, i, k]}")
            
            # compute a
            for i in range(1, j):
                for k in range(j, m):
                    if gamma(m, i-1) < 1 or gamma(m, k-1) < j:
                        a[m, j, i, k] = a[m-1, j, i, k]
                    else:
                        a[m, j, i, k] = min(a[m-1, j, i, k], h[m, j, i, k])
                    if seq[i-1] == seq[k-1] == seq[m-1]:
                        if gamma(m, i-1) < 1 or gamma(m, k-1) < j:
                            a[m, j, i, k] = m
                        else:
                            a[m, j, i, k] = h[m, j, i, k]
                    elif seq[i-1] == seq[m-1]:
                        if gamma(m, k-1) >= j:
                            a[m, j, i, k] = max(a[m, j, i, k], a[m, j, i, gamma(m, k - 1)])
                    elif seq[k-1] == seq[m-1]:
                        if gamma(m, i-1) >= 1:
                            a[m, j, i, k] = max(a[m, j, i, k], a[m, j, gamma(m, i-1), k])
                    
                    print(f"a[{m}, {j}, {i}, {k}] = {a[m, j, i, k]}")
        
test()