cpdef int run(str seq, str pattern):
    cdef:
        unsigned int n, m, i, k

    n, m = len(seq), len(pattern)

    for i in range(n - m + 1):
        k = 0
        while k < m and seq[i + k] == pattern[k]:
            k += 1
        if k == m:
            return i
    return -1
