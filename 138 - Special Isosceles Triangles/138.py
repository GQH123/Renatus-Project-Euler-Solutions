# Problem 138. Special Isosceles Triangles
# Link: https://projecteuler.net/problem=138
# Answer: 1118049290473932
# Language: Python
# Author: Renatus
# Date: 2025-08-30 12:01:53

from functools import lru_cache
from gmpy2 import get_context, isqrt


def solve():
    """
        We know 4L^2 = b^2 + 4(b + 1)^2 or 4L^2 = b^2 + 4(b - 1)^2 holds. By using Alpertron Calculator (https://www.alpertron.com.ar/QUAD.HTM), we can get the solutions of the equation.
        
        - For 4L^2 = b^2 + 4(b + 1)^2: 
        
            5x² - 4y² + 8x + 4 = 0
            x = 0
            y = 1

            Recursive solutions:

            x_{n+1} = - 9x_n + 8y_n - 8
            y_{n+1} = 10x_n - 9y_n + 8

            and also:

            x_{n+1} = - 9x_n - 8y_n - 8
            y_{n+1} = - 10x_n - 9y_n - 8
        
        - For 4L^2 = b^2 + 4(b - 1)^2: 
        
            5x² - 4y² - 8x + 4 = 0
            x = 0
            y = -1

            Recursive solutions:

            x_{n+1} = - 9x_n + 8y_n + 8
            y_{n+1} = 10x_n - 9y_n - 8

            and also:

            x_{n+1} = - 9x_n - 8y_n + 8
            y_{n+1} = - 10x_n - 9y_n + 8
        
        Simple roll out enough solutions, filter the correct ones and sort them, we can get the answer.
    """
    
    context = get_context()
    context.precision = 100000
    
    solutions = set()
    
    # for h = b + 1, recursive case 1
    b, L = 0, 1
    for i in range(1000):
        if b > 0 and L > 0 and (b & 1 == 0):
            v = L**2 - b**2//4
            h = isqrt(v)
            if h**2 == v and h == b + 1:
                solutions.add((b, L, int(h)))
        b, L = -9 * b + 8 * L - 8, 10 * b - 9 * L + 8
    
    # for h = b + 1, recursive case 2
    b, L = 0, 1
    for i in range(1000):
        if b > 0 and L > 0 and (b & 1 == 0):
            v = L**2 - b**2//4
            h = isqrt(v)
            if h**2 == v and h == b + 1:
                solutions.add((b, L, int(h)))
        b, L = -9 * b - 8 * L - 8, -10 * b - 9 * L - 8
    
    # for h = b - 1, recursive case 1
    b, L = 0, -1
    for i in range(1000):
        if b > 0 and L > 0 and (b & 1 == 0):
            v = L**2 - b**2//4
            h = isqrt(v)
            if h**2 == v and h == b - 1:
                solutions.add((b, L, int(h)))
        b, L = -9 * b + 8 * L + 8, 10 * b - 9 * L - 8
    
    # for h = b - 1, recursive case 2
    b, L = 0, -1
    for i in range(1000):
        if b > 0 and L > 0 and (b & 1 == 0):
            v = L**2 - b**2//4
            h = isqrt(v)
            if h**2 == v and h == b - 1:
                solutions.add((b, L, int(h)))
        b, L = -9 * b - 8 * L + 8, -10 * b - 9 * L + 8
    
    solutions = list(sorted(solutions, key = lambda x: x[0]))[:12]
    print(solutions)
    print(sum([x[1] for x in solutions]))


if __name__ == '__main__':
    solve()
    pass
