import numpy as np

# fix j and m, we want to compute a(i, k) matrices
# outer loop over m 
# next over j 
# over k
# over i 
# use temp h value, not stored 

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
    if i >= 1 and i < j and j <= k and k < m:
        if seq[i-1] == seq[k-1] == seq[m-1]:
            return h_func(i, k, j, m-1, seq)
        return min(a_func(i, k, j, m-1, seq), h_func(i, k, j, m-1, seq))
    else:
        return 0

# assume we have a_{m}^{j}(r, s) where \gamma_{m}(i-1) <= r <= i-1 and 
# \gamma_{m}(k-1) <= s <= k-1
def h_func(i, k, j, m, seq):
    print(f"h_func entered. i: {i}, k: {k}, j: {j}, m: {m}")
    x = gamma(m, i-1, seq)
    y = gamma(m, k-1, seq)
    if x < 0 or y <= i:
        return m
    elif x < i-1:
        if y < k-1:
            return a_func(i-1, k-1, j, m-1, seq)
        return max(a_func(i-1, k-1, j, m-1, seq), h_func(i-1, k, j, m, seq))
    elif y < k-1:
        return max(a_func(i-1, k-1, j, m-1, seq), h_func(i, k-1, j, m, seq))
    else:
        return max(a_func(i-1, k-1, j, m-1, seq), h_func(i-1, k, j, m, seq), h_func(i, k-1, j, m, seq))

# returns a_func matrix for a given j and m
def helper(j, m, seq):
    a_matrix = np.zeros((m+1, m+1), dtype=int)
    # makes first row and column -1s to indicate that they should be ignored
    a_matrix[0] = -1
    a_matrix[:, 0] = -1
    # fill in a_matrix for appropriate values of i and k
    for i in range(1, j):
        for k in range(j, m):
            a_matrix[i, k] = a_func(i, k, j, m, seq)
    return a_matrix

# prints m and j values in heading and appropriate j and m matrices
def print_matrices(word):
    for m in range(1, len(word)+1):
        for j in range(2, m):
            print(f"\nm: {m}, j: {j}")
            print(helper(j, m, word))

w = "abcadbaby"
print(a_func(2, 7, 5, 9, w))
# print_matrices(w)
