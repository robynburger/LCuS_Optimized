import numpy as np

# fix j and m, we want to compute a(i, k) matrices
# outer loop over m 
# next over j 
# over k
# over i 
# use temp h value, not stored 
#

# gamma_{m}(x) is the largest value of r such that r <= x and 
# seq[r] == seq[m], or 0 if no such value exists
def gamma(m, x, seq):
    for r in range(x, 0, -1):
        if seq[r-1] == seq[m-1]:
            return r
    return 0

# assume we have a_{m-1}^{j}(i, k) 
# for 1 to m-1
def a_func(i, k, j, m, seq):
    print(f"a_func entered. i: {i}, k: {k}, j: {j}, m: {m}")
    if 1 <= i and i < j and j <= k and k < m:
        if seq[i-1] == seq[k-1] == seq[m-1]:
            return h_func(i, k, j, m, seq)
        return min(a_func(i, k, j, m-1, seq), h_func(i, k, j, m, seq))
    else:
        return 0

# assume we have a_{m}^{j}(r, s) where \gamma_{m}(i-1) <= r <= i-1 and 
# \gamma_{m}(k-1) <= s <= k-1
def h_func(i, k, j, m, seq):
    print(f"h_func entered. i: {i}, k: {k}, j: {j}, m: {m}")
    x = gamma(m, i-1, seq)
    y = gamma(m, k-1, seq)
    if x == 0 or y == 0:
        return m
    curr_max = 0
    for r in range(x, i):
        for s in range(y, k):
            # maybe this should be a(r, s, j, m-1) ?
            temp_max = a_func(r, s, j, m, seq)
            if temp_max > curr_max:
                curr_max = temp_max
    return curr_max

def helper(i, k, j, m, seq):
    # print(f"output: {a_func(i, k, j, m, seq)}")
    a_matrix = np.zeros((m+1, m+1), dtype=int)
    for a in range(1, j):
        for b in range(j+1, m):
            a_matrix[a, b] = a_func(a, b, j, m, seq)
    print(a_matrix)


helper(2, 7, 5, 9, "abcadbaby")
