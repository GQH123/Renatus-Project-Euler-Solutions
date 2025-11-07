# Problem 128. Hexagonal Tile Differences
# Link: https://projecteuler.net/problem=128
# Answer: 14516824220
# Language: Python
# Author: Renatus
# Date: 2025-08-29 17:04:21

from math import sqrt
from functools import lru_cache


@lru_cache(maxsize=None)
def simple_check_prime(p):
    if p < 2:
        return False
    
    # simple optimization for large primes
    if p > int(1e7):
        p_str = str(p)
        if sum([int(c) for c in p_str]) % 3 == 0:
            return False
        if p_str[-1] in ['0', '2', '4', '5', '6', '8']:
            return False
    
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    
    return True


def traverse_corner():
    N = 2000
    pc = 1
    x = 2
    d = 1
    c = 6
    while True:
        if x == 17:
            print(x, d, c)
            return
        cp = 0
        cp += simple_check_prime(6 * d + 6 - c)
        cp += simple_check_prime(6 * d + 6 - c + 1)
        cp += simple_check_prime(6 * d + 6 - c - 1)
        cp += simple_check_prime(max(6 * (d - 1) + 6 - c, 1))
        cp += simple_check_prime(1)
            
        if c == 6:
            if x != 8:  # exclude 8 as the special case
                # the tile before the special corner
                _cp = cp - simple_check_prime(6 * d + 6 - c + 1)
                _cp += simple_check_prime(c * (d - 1) - 1)
                _cp += simple_check_prime(c * (d + d - 3) - 1)
                if _cp == 3:
                    pc += 1
                    print(f'found {pc}-th PD=3 tile {x-1}')
                    if pc == N:
                        break
            # special corner
            cp += simple_check_prime(c * (d + d + 1) - 1)
        else:
            # normal corner
            cp += simple_check_prime(1)
        
        if cp == 3:
            pc += 1
            print(f'found {pc}-th PD=3 tile {x}')
            if pc == N:
                break
        
        x += d
        c -= 1
        if c == 0:
            d += 1
            c = 6


if __name__ == '__main__':
    traverse_corner()
    pass
