# Problem 125. Palindromic Sums
# Link: https://projecteuler.net/problem=125
# Answer: 2906969179
# Language: Python
# Author: Renatus
# Date: 2025-08-29 12:48:27

import math
from functools import lru_cache


def check_palindrome_number(x):
    return str(x) == str(x)[::-1]


def brute_force():
    valid_number_set = set()
    for s in range(1, int(1e4)):
        current_sum = s ** 2 + (s + 1) ** 2
        i = s + 1
        while current_sum < int(1e8):
            if check_palindrome_number(current_sum):
                if current_sum in valid_number_set:
                    print(f'warning: {current_sum} appears more than once')
                valid_number_set.add(current_sum)
            i += 1
            current_sum += i ** 2
    # print(valid_number_set)
    print(f'sum of all valid palindromic sums is {sum(valid_number_set)}, found {len(valid_number_set)} valid numbers')


if __name__ == '__main__':
    brute_force()
    pass
