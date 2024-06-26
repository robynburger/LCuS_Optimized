import numpy as np

# gamma(m, x, seq) is the largest value of r such that r <= x and 
# seq[r] == seq[m], or 0 if no such value exists
def gamma(m, x, seq):
    for r in range(x, 0, -1):
        if seq[r-1] == seq[m-1]:
            return r
    return 0

def naive(seq):
    n = len(seq)
    f = np.zeros((n+1, n+1, n+1, n+1, n+1), dtype=int)      # f[m,j,i,k,l]
    A = np.zeros((n+1, n+1, n+1, n+1), dtype=int)      # A[m,j,i,k]
    for m in range(1, n+1):
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                for k in range(j, n+1):
                    for l in range(k+1, m+1):
                        f[m, j, i, k, l] = f[m - 1, j, i, k, l]
                        if gamma(m, i, seq) > 0 and gamma(m, k, seq) >= j:
                            f[m, j, i, k, l] = max(f[m, j, i, k, l], f[m-1, j, gamma(m, i, seq)-1, gamma(m, k, seq)-1, l]+1)
                        if f[m, j, i, k, l] > f[m, j, i-1, k-1, l] and seq[i-1] == seq[k-1]:
                            A[m, j, i, k] = l
                            #print(f"d[{m}, {j}, {i}, {k}, {l}] = 1")
                    #if A[m,j,i,k] > 0:
                        #print(f"A[{m}, {j}, {i}, {k}] = {A[m,j,i,k]}")
    return A