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
    for r in range(0, x+1, -1):
        if seq[r] == seq[m]:
            return r
    return 0

# assume we have a_{m-1}^{j}(i, k) 
# for 1 to m-1
def a_func(i, k, j, m, seq):
    print(f"a_func entered. i: {i}, k: {k}, j: {j}, m: {m}")
    if seq[i] == seq[k] == seq[m]:
        return h_func(i, k, j, m, seq)
    if m >= 3:
        return min(a_func(i, k, j, m-1, seq), h_func(i, k, j, m, seq))
    else:
        return 0

# assume we have a_{m}^{j}(r, s) where \gamma_{m}(i-1) <= r <= i-1 and 
# \gamma_{m}(k-1) <= s <= k-1
def h_func(i, k, j, m, seq):
    print(f"h_func entered. i: {i}, k: {k}, j: {j}, m: {m}")
    if gamma(m, i-1, seq) == 0 or gamma(m, k-1, seq) == 0:
        return m
    max_a_m_j = 0
    for r in range(gamma(m, i-1, seq), i):
        for s in range(gamma(m, k-1, seq), k):
            if a_func(r, s, j, m, seq) > max_a_m_j:
                max_a_m_j = a_func(r, s, j, m, seq)
    return max_a_m_j

print(a_func(3, 6, 5, 8, "abcdacad"))