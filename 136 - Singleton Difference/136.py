# Problem 136. Singleton Difference
# Link: https://projecteuler.net/problem=136
# Answer: 2544559
# Language: Python
# Author: Renatus
# Date: 2025-08-30 00:37:29

from math import ceil
from functools import lru_cache
from tqdm import tqdm


def _enumerate_n_and_divisors_deprecated():
    N = int(5e7)
    # N = int(1e2)
    count = 0
    for n in tqdm(range(1, N)):
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
            if n_solution > 1:
                break
        if n_solution == 1:
            count += 1
            # print(f'found {count}-th n={n} with 1 solutions')
    print(count)


def enumerate_y_and_common_difference():  # this is significantly faster, O(Σ(n/i)) = O(nlogn)
    N = int(5e7)
    # N = int(1e2)
    n_solutions = [0] * N
    count = 0
    for y in tqdm(range(1, N)):
        for p in range(ceil(y/4), y):
            v = y * (4 * p - y)
            if v >= N:
                break
            n_solutions[v] += 1
    for n_solution in n_solutions:
        if n_solution == 1:
            count += 1
    print(count)


if __name__ == '__main__':
    # enumerate_n_and_divisors()
    enumerate_y_and_common_difference()
    pass
