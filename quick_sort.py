from random import randint

from core import quick_sort


def run(seq):
    print(quick_sort.run(seq), '<- sorted list.')


if __name__ == '__main__':
    import cProfile

    sequence = [randint(0, 100) for _ in range(1000)]

    cProfile.run('run(sequence)', sort='time')
