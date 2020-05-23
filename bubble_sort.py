from pytictoc import TicToc

from core import bubble_sort

seq = [10, 77, 80, 61, 36, 1, 36, 36, 5, 23, 72, 35, 41, 75, 23, 16, 97, 68, 44, 65, 59, 11, 73, 78, 53, 70, 53, 2, 64,
       41, 97, 12, 47, 91, 44, 97, 81, 67, 99, 13, 66, 92, 52, 88, 73, 39, 29, 55, 25, 43, 43, 52, 47, 22, 60, 3, 53,
       66, 96, 66, 9, 7, 25, 24, 17, 45, 54, 16, 63, 67, 98, 1, 2, 75, 93, 59, 52, 1, 67, 22, 83, 28, 13, 29, 66, 40,
       12, 85, 77, 87, 84, 64, 72, 43, 60, 67, 92, 75, 95, 18, 9, 97, 7, 54, 80, 46, 45, 67, 23, 67, 35, 33, 49, 17, 74,
       53, 61, 14, 16, 64, 61, 70, 35, 81, 36, 46, 92, 30, 29, 90, 5, 33, 71, 40, 44, 80, 97, 85, 64, 52, 80, 65, 81,
       61, 51, 20, 43, 58, 16, 30, 78, 80, 3, 36, 99, 7, 13, 88, 76, 19, 91, 91, 26, 63, 97, 32, 62, 36, 13, 24, 88, 21,
       89, 89, 77, 92, 68, 5, 86, 86, 56, 79, 0, 71, 87, 77, 48, 11, 76, 65, 66, 75, 76, 43, 65, 72, 58, 42, 56, 48, 59,
       93, 53, 100, 90, 85, 40, 9, 48, 52, 12, 3, 44, 83, 92, 58, 94, 58, 78, 72, 23, 84, 46, 16, 89, 3, 37, 35, 14, 84,
       49, 46, 50, 21, 34, 89, 81, 81, 57, 34, 60, 40, 63, 23, 32, 99, 6, 59, 53, 30, 43, 75, 86, 41, 61, 33, 94, 26,
       54, 2, 36, 47, 66, 48, 10, 43, 76, 46, 77, 62, 22, 81, 6, 66, 3, 8, 56, 77, 95, 50, 14, 27, 4, 42, 37, 40, 7, 49,
       28, 25, 4, 30, 51, 25, 97, 69, 21, 36, 64, 40, 69, 49, 39, 97, 85, 26, 47, 44, 27, 48, 93, 19, 70, 79, 21, 34,
       25, 1, 66, 61, 80, 0, 25, 99, 42, 61, 89, 12, 61, 89, 12, 52, 31, 53, 56, 61, 4, 20, 15, 57, 88, 88, 64, 55, 95,
       47, 91, 81, 66, 3, 37, 41, 3, 35, 59, 94, 28, 65, 17, 30, 45, 22, 49, 89, 70, 26, 55, 97, 59, 0, 61, 21, 70, 61,
       82, 65, 40, 79, 5, 40, 90, 76, 39, 79, 49, 85, 76, 80, 56, 48, 41, 6, 79, 56, 37, 55, 23, 38, 64, 29, 71, 92, 7,
       96, 96, 2, 54, 91, 45, 71, 45, 26, 13, 20, 92, 76, 90, 98, 40, 42, 83, 11, 57, 79, 94, 54, 72, 66, 35, 60, 60,
       27, 58, 80, 76, 79, 59, 3, 44, 39, 87, 75, 79, 44, 1, 9, 14, 85, 61, 9, 24, 1, 85, 6, 17, 88, 8, 62, 61, 37, 8,
       62, 51, 21, 14, 0, 76, 71, 91, 17, 95, 39, 26, 51, 94, 18, 89, 69, 42, 77, 34, 94, 69, 52, 83, 30, 20, 37, 31,
       17, 8, 72, 77, 5, 41, 46, 82, 79, 51, 42, 77, 43, 36, 30, 93, 11, 27, 1, 56, 99, 22, 17, 72, 46, 90, 63, 22, 50,
       87, 5, 49, 86, 77, 1, 46, 42, 43, 76, 70, 89, 5, 43, 81, 71, 40, 48, 94, 44, 64, 5, 89, 33, 59, 90, 76, 80, 10,
       34, 52, 78, 73, 17, 34, 61, 73, 74, 36, 87, 63, 93, 90, 10, 94, 3, 85, 65, 98, 27, 46, 60, 62, 2, 11, 5, 23, 31,
       61, 74, 91, 3, 94, 92, 79, 64, 53, 35, 66, 58, 56, 76, 91, 96, 68, 56, 21, 7, 61, 76, 82, 6, 8, 34, 22, 4, 54,
       31, 49, 61, 54, 12, 46, 56, 18, 70, 12, 81, 19, 86, 25, 78, 11, 54, 86, 61, 0, 49, 43, 2, 96, 23, 82, 54, 0, 23,
       15, 2, 22, 72, 96, 63, 98, 67, 18, 42, 33, 31, 84, 7, 1, 75, 42, 45, 28, 21, 64, 13, 98, 74, 90, 98, 22, 75, 59,
       55, 29, 6, 54, 78, 10, 28, 64, 60, 42, 38, 89, 28, 50, 28, 38, 52, 18, 47, 80, 69, 51, 81, 61, 2, 88, 81, 24, 76,
       55, 22, 49, 4, 86, 22, 27, 52, 21, 36, 81, 15, 23, 81, 36, 66, 100, 66, 80, 33, 67, 56, 33, 80, 83, 55, 16, 54,
       78, 65, 25, 44, 23, 50, 45, 45, 4, 51, 67, 22, 65, 90, 92, 28, 99, 32, 84, 15, 58, 66, 70, 19, 55, 13, 41, 39,
       49, 18, 25, 70, 72, 85, 70, 38, 58, 26, 70, 23, 12, 7, 42, 18, 68, 96, 39, 12, 65, 100, 76, 92, 11, 69, 65, 14,
       51, 26, 64, 10, 74, 59, 15, 55, 77, 9, 44, 94, 83, 29, 35, 20, 28, 98, 97, 85, 30, 80, 97, 53, 80, 1, 19, 23, 80,
       15, 99, 15, 77, 93, 27, 97, 53, 36, 26, 0, 93, 21, 4, 42, 63, 60, 0, 88, 6, 23, 5, 12, 85, 75, 18, 23, 9, 59, 81,
       66, 33, 45, 64, 38, 15, 88, 91, 52, 67, 49, 96, 8, 3, 77, 87, 8, 79, 45, 9, 65, 96, 84, 32, 95, 54, 57, 39, 81,
       51, 15, 20, 71, 98, 76, 58, 32, 49, 7, 27, 14, 29, 81, 51, 4, 80, 0, 33, 82, 4, 5, 25, 95, 69, 65, 8, 76, 48, 95,
       51, 21, 10, 57, 5, 10, 48, 34, 1, 86, 30, 33, 4, 0, 51, 100, 70, 93, 2, 13, 59, 72, 54, 1, 87, 11, 43, 66, 40,
       79, 49, 83, 29, 59, 1, 69, 59, 9, 29, 59, 55, 4, 97, 41, 27, 28, 75, 85, 47, 59, 11, 42, 68, 8, 53, 57, 30, 87,
       3, 64, 5, 35, 39, 16, 14, 81, 73, 22, 68, 64, 2, 36, 30, 28, 74, 60, 60, 34, 14, 14, 10, 13, 74, 65, 42, 93, 58,
       44, 46, 27, 28, 36, 42, 9, 74, 96, 33, 79, 26, 18, 26, 32, 47, 62, 47, 46, 43, 76, 26, 49, 68, 66, 76, 32, 68,
       17, 21, 3, 32, 22, 51, 92, 77, 40, 85, 78, 18, 76, 75, 51, 48, 57, 53, 67, 37, 56, 61, 81, 30, 40, 95, 85, 15,
       70, 71, 64, 23, 37, 20, 58, 15, 25, 16, 31, 34, 31, 25, 22, 31, 100, 0, 4, 1, 28, 60, 13, 61, 100, 55, 66, 28,
       75, 97, 9, 91, 81, 89, 58, 29, 12, 62, 49, 89, 47, 75, 10, 34, 73, 13, 11, 92, 53, 23, 19, 86, 6, 62, 87, 22, 17,
       69, 61, 18, 60, 55, 54, 92, 6, 72, 10, 1, 19, 72, 28, 10, 100, 2, 8, 26, 15, 54, 2, 76, 95, 99, 72, 81, 12, 42,
       53, 50, 53, 74, 37, 19, 76, 37, 96, 13, 77, 64, 4, 90, 33, 33, 77, 85, 82, 48, 81, 70, 24, 99, 32, 72, 46, 96,
       16, 70, 58, 93, 7, 60, 64, 54, 56, 52, 45, 48, 26, 97, 15, 60, 31, 10, 84, 41, 60, 9, 2, 41, 11, 23, 24, 27, 41,
       69, 94, 62, 91, 64, 61, 100, 30, 74, 14, 71, 42, 48, 100, 65, 88, 88, 12, 0, 43, 66, 8, 77, 34, 9, 5, 97, 60, 50,
       98, 92, 93, 87, 72, 6, 4, 86, 96, 61, 86, 89, 18, 100, 22, 39, 24, 52, 78, 90, 14, 15, 35, 35, 45, 49, 60, 67]


def run():
    with TicToc():
        sorted = bubble_sort.run(seq)

        print(sorted, '<- sorted list.')


if __name__ == '__main__':
    run()
