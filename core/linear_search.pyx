cpdef run(list seq, int target):
    cdef int index, item

    for index, item in enumerate(seq):
        if item == target:
            return index
    return None
