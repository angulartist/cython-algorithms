cpdef list run(list collection):
    cdef:
        int length = len(collection)
        int pivot, element
        list greater, lesser

    if length <= 1:
        return collection
    else:
        pivot = collection.pop()
        greater, lesser = [], []

        for element in collection:
            if element > pivot:
                greater.append(element)
            else:
                lesser.append(element)

        return run(lesser) + [pivot] + run(greater)
