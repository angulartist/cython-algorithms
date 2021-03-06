cpdef list run(list collection):
    cdef:
        unsigned int length = len(collection)
        unsigned int i, j
        bint swapped

    for i in range(length - 1):
        swapped = False

        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break

    return collection
