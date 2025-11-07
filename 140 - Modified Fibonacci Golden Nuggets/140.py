# Problem 140. Modified Fibonacci Golden Nuggets
# Link: https://projecteuler.net/problem=140
# Answer: 5673835352990
# Language: Python
# Author: Renatus
# Date: 2025-08-30 14:08:50

import math
from functools import lru_cache


def solve():
    """
        It can be shown that 5n^2+14n+1 = t^2, we can get all solutions of the equation by using Alpertron Calculator (https://www.alpertron.com.ar/QUAD.HTM).
        
        5x² - y² + 14x + 1 = 0
        
        x = 2
        y = -7

        and also:
        x = 0
        y = -1

        and also:
        x = 0
        y = 1

        and also:
        x = -4
        y = 5

        and also:
        x = -3
        y = 2

        and also:
        x = -3
        y = -2

        Recursive solutions:

        x_{n+1} = - 9x_n - 4y_n - 14
        y_{n+1} = - 20x_n - 9y_n - 28

        and also:

        x_{n+1} = - 9x_n + 4y_n - 14
        y_{n+1} = 20x_n - 9y_n + 28
    """
    solutions = set()
    for n, t in [(2, -7), (0, -1), (0, 1), (-4, 5), (-3, 2), (-3, -2)]:
        for f_recursive in [
            lambda x, y: (-9 * x - 4 * y - 14, -20 * x - 9 * y - 28),
            lambda x, y: (-9 * x + 4 * y - 14, 20 * x - 9 * y + 28),
        ]:
            for _ in range(1000):
                if n > 0:
                    solutions.add(n)
                n, t = f_recursive(n, t)
    solutions = sorted(solutions)[:30]
    print(solutions)
    print(sum(solutions))


if __name__ == '__main__':
    solve()
    pass
