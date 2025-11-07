# Problem 126. Cuboid Layers
# Link: https://projecteuler.net/problem=126
# Answer: 18522
# Language: Python
# Author: Renatus
# Date: 2025-08-29 13:00:23

import math
from tqdm import tqdm
from functools import lru_cache


C = []


def brute_force():
    N = 50000  # assume the answer n is less than N
    global C
    C = [0] * N
    for a in tqdm(range(N - 1, 0, -1)):
        if 6 * a * a >= N:
            continue
        for b in range(a, N):
            if 2 * (a * b + b * b + a * b) >= N:
                break
            for c in range(b, N):
                if 2 * (a * b + b * c + a * c) >= N:
                    break
                # now we get an initial cuboid measuring a * b * c
                
                middle_layer_count = a  # we choose dimension along 'a' as the middle layer
                middle_layer_size = b * c
                middle_layer_perimeter = 2 * (b + c) - 4
                
                while True:
                    middle_layer_size_delta = middle_layer_perimeter + 4
                    next_layer_cube_count = 2 * middle_layer_size + middle_layer_count * middle_layer_size_delta
                    if next_layer_cube_count >= N:
                        break
                    else:
                        C[next_layer_cube_count] += 1
                    middle_layer_size += middle_layer_size_delta
                    middle_layer_perimeter = middle_layer_size_delta
    
    
    max_C = -1
    max_C_index = -1
    if_found = False
    for c_index, c_value in enumerate(C):
        if max_C < c_value:
            max_C = c_value
            max_C_index = c_index
        if not if_found and c_value == 1000:
            print(f'least value of c for which C[c] = 1000 is {c_index}')
            if_found = True
        
    print(C[22], C[46], C[78], C[118])
    print(f'C[{max_C_index}] = {max_C} is the maximum C value in [1, {N})')


if __name__ == '__main__':
    brute_force()
    pass
