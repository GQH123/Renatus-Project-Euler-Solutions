# Problem Bonus. Heegner
# Link: https://projecteuler.net/problem=heegner
# Answer: -163
# Language: Python
# Author: Renatus
# Date: 2025-08-29 13:02:58

from gmpy2 import get_context, isqrt, cos, const_pi, sqrt, floor


def simple_brute_force():
    ctx = get_context()
    ctx.precision = 1000
    ctx.allow_complex = True
    
    min_distance = 1000**2
    min_distance_n = -1
    for i in range(-1000, 1001):
        if i >= 0 and int(isqrt(i)) ** 2 == i:
            continue
        f_v = cos(const_pi() * sqrt(i)).real
        i_v = floor(f_v)
        if abs(f_v - i_v) < min_distance:
            min_distance = abs(f_v - i_v)
            min_distance_n = i
        if abs(f_v - (i_v + 1)) < min_distance:
            min_distance = abs(f_v - (i_v + 1))
            min_distance_n = i
        
        # print(f'{i} leads to distance {min(abs(f_v - i_v), abs(f_v - (i_v + 1))):.100f}')
    
    print(f'{min_distance_n} leads to minimum distance {min_distance:.100f}')
    # 962 leads to minimum distance 0.0012828256154242546


if __name__ == '__main__':
    simple_brute_force()
    pass
