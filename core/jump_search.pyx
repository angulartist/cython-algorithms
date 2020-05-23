import math

cpdef run(list arr, int x):
    cdef:
        int n = len(arr)
        int step = int(math.floor(math.sqrt(n)))
        int prev = 0

    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.floor(math.sqrt(n)))

        if prev >= n:
            return -1

    while arr[prev] < x:
        prev = prev + 1
        if prev == min(step, n):
            return -1

    if arr[prev] == x:
        return prev

    return -1
