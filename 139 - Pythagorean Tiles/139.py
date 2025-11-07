# Problem 139. Pythagorean Tiles
# Link: https://projecteuler.net/problem=139
# Answer: 10057761
# Language: Python
# Author: Renatus
# Date: 2025-08-30 13:37:03

from math import gcd
from functools import lru_cache
from tqdm import tqdm


def solve():
    """
        We know a^2 + b^2 = c^2 (a < b < c) and (b - a) | c. Set c = k(b - a), we get (k^2-1)a^2 - 2k^2ab + (k^2-1)b^2 = 0, so 8k^2 - 4 = 4t^2, 2k^2 - t^2 - 1 = 0. From Alpertron Calculator (https://www.alpertron.com.ar/QUAD.HTM), we can get the solutions of the equation.
        
        2x² - y² - 1 = 0
        
        x = -1
        y = 1

        and also:
        x = 1
        y = -1

        Recursive solutions:

        x_{n+1} = 3x_n + 2y_n
        y_{n+1} = 4x_n + 3y_n

        and also:

        x_{n+1} = 3x_n - 2y_n
        y_{n+1} = - 4x_n + 3y_n

        The constraints are k > 1 and can find corresponding a, b, c. So we can get all answers after filtering.
    """
    
    solutions = set()
    
    for k, t in [(-1, 1), (1, -1)]:
        for f_recursive in [
            lambda x, y: (3 * x + 2 * y, 4 * x + 3 * y),
            lambda x, y: (3 * x - 2 * y, -4 * x + 3 * y),
        ]:
            for _ in range(1000):
                if k > 1 and t > 0:
                    solutions.add((k, t))
                k, t = f_recursive(k, t)
    
    N = int(1e8)
    answers = set()
    for k, t in tqdm(solutions):
        numerator = 2 * (k**2 - t)
        denominator = 2 * (k**2 - 1)
        d = gcd(numerator, denominator)
        numerator //= d
        denominator //= d
        for b in range(denominator, N, denominator):
            a = numerator * b // denominator
            c = (b - a) * k
            assert a * a + b * b == c * c
            if (a + b + c < N):
                answers.add((a, b, c))
    # print(answers)
    print(len(answers))


if __name__ == '__main__':
    solve()
    pass
