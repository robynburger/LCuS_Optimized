import os
import numpy as np

'''
HOW TO USE THIS DRAFT: 

In final line:  'print_A(3, "ababab")', replace '3' with your j-value and 
"ababab" with your sequence. 

Your results will be in results/sequence/j.txt So, the output of 
'print_A(3, "ababab")' would be found in results/ababab/3.txt

'''


# gamma(m, x, seq) is the largest value of r such that r <= x and 
# seq[r] == seq[m], or 0 if no such value exists
def gamma(m, x, seq):
    for r in range(x, 0, -1):
        if seq[r-1] == seq[m-1]:
            return r
    return 0

# for a fixed j, populate_A produces a list of matricies, where the i^th matrix
# corresponds to the value of h_i^j(i, k)
def populate_A(A, j, seq):
    n = len(seq)
    for m in range(1, n+1):
        for i in range(1, m+1):
            for k in range(j, m):
                if 1 <= i and i < j and j <= k and k < m:
                        #  A[m, i, k] = 101 # high value that will never be the min
                    if seq[i-1] == seq[k-1] == seq[m-1]:
                        A[m, i, k] = h_func(i, k, j, m, seq, A)
                    elif k == m-1:
                        A[m, i, k] = k
                    else:
                        A[m, i, k] = min(A[m-1, i, k], h_func(i, k, j, m, seq, A))
    return A

# h_func(i, k, j, m, seq, A) recursively calculates the value of h_m^j(i, k)
def h_func(i, k, j, m, seq, A):
    # if i >= 1 and i < j and j <= k and k < m:
    g_i = gamma(m, i-1, seq)
    g_k = gamma(m, k-1, seq)
    if g_i < 1 or g_k <= i:
        return m
    h_i = h_func(i-1, k, j, m, seq, A)
    h_k = h_func(i, k-1, j, m, seq, A)
    if g_i == i-1:
        h_i = -1
    if g_k == k-1:
        h_k = -1
    return max(A[m-1, i-1, k-1], h_i, h_k)
    
    #else:
        #return 0

# print_A(j, seq) prints an n by n matrix for each value of m, which holds the 
# values of a_m^j(i, k) for a fixed j
def print_A(j, seq):
    n = len(seq)
    A = populate_A(np.zeros((n+1, n+1, n+1), dtype=int) + 100, j, seq)
    # print(A)
    file_name = str(f"results/{seq}/{j}.txt")
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    file = open(file_name, "w")
    # display string and i, j, k, l, m parameters
    file.write("\n Note: top row and left column are buffers to account for 1-based indexing")
    file.write("\n and values of 100 are null\n\n")
    file.write(f"\ns = {seq}\n")
    file.write(f"j = {j}\n\n")

    eq_signs = (len(seq)+10) * "="
    file.write(f"{eq_signs} A {eq_signs}\n")
    for m in range(1, len(A)): # change this line if you want m = 0 matrix to print 
        file.write(f"\n\nm = {m} \n{str(A[m])}") 
    file.close()
    

'''
EDIT THE LINE BELOW TO RUN THE PROGRAM:
'''
print_A(5, "abcadbaby")

  













"""
# assume we have a_{m-1}^{j}(i, k) 
# for 1 to m-1
def a_func(i, k, j, m, seq):
    # print(f"a_func entered. i: {i}, k: {k}, j: {j}, m: {m}")
    if i >= 1 and i < j and j <= k and k < m:
        if seq[i-1] == seq[k-1] == seq[m-1]:
            return h_func(i, k, j, m-1, seq)
        return min(a_func(i, k, j, m-1, seq), h_func(i, k, j, m-1, seq))
    else:
        return 0

# assume we have a_{m}^{j}(r, s) where \gamma_{m}(i-1) <= r <= i-1 and 
# \gamma_{m}(k-1) <= s <= k-1
def h_func(i, k, j, m, seq):
    # print(f"h_func entered. i: {i}, k: {k}, j: {j}, m: {m}")
    if i >= 1 and i < j and j <= k and k < m:
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
    else:
        return 0

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

"""
# w = "abcadbaby"
# print_matrices(w)

