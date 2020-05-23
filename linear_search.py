from random import randint

from pytictoc import TicToc

from core import linear_search

s_min = 0
s_max = 100
s_len = 10000
seq = [randint(s_min, s_max) for _ in range(s_len)]
target = randint(s_min, s_max)


def run():
    print('Generated sequence=', seq)

    with TicToc():
        idx = linear_search.run(seq, target)
        print('Found target=', target, 'at index=', idx)


if __name__ == '__main__':
    run()
