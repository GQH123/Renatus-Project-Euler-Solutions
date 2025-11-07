# Problem 135. Same Differences
# Link: https://projecteuler.net/problem=135
# Answer: 4989
# Language: Python
# Author: Renatus
# Date: 2025-08-30 00:18:37

import math
from functools import lru_cache


def enumerate_n_and_divisors():
    N = int(1e6)
    count = 0
    for n in range(1, N):
        if n % 4 not in [0, 3]:
            continue
        n_solution = 0
        for i in range(1, n):
            if i * i > n:
                break
            if n % i != 0:
                continue
            x, y = i, n // i
            if (x + y) % 4 == 0:
                if x > (x + y) // 4:
                    n_solution += 1
                if x != y and y > (x + y) // 4:
                    n_solution += 1
            if n_solution > 10:
                break
        if n_solution == 10:
            count += 1
            print(f'found {count}-th n={n} with 10 solutions')
    print(count)


if __name__ == '__main__':
    enumerate_n_and_divisors()
    pass
