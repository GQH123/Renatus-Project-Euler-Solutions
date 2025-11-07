# Problem 127. abc-hits
# Link: https://projecteuler.net/problem=127
# Answer: 18407904
# Language: Python
# Author: Renatus
# Date: 2025-08-29 15:49:25

import sys

sys.setrecursionlimit(1000000)

from math import gcd, sqrt
from functools import lru_cache

min_prime_index = []
max_prime_index = []
is_prime = []
primes = []


# Euler's Prime Sieve
def preprocess_primes(n=int(1e6)):  # sieve all primes in [1, n]
    global min_prime_index, max_prime_index, primes, is_prime
    min_prime_index = [-1] * (n + 1)
    max_prime_index = [-1] * (n + 1)
    is_prime = [True] * (n + 1)
    primes = []
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            min_prime_index[i] = len(primes) - 1
            max_prime_index[i] = len(primes) - 1
        for p_index, p in enumerate(primes):
            if i * p > n:
                break
            is_prime[i * p] = False
            min_prime_index[i * p] = p_index
            max_prime_index[i * p] = max_prime_index[i]
            if i % p == 0:
                break


radical = []


@lru_cache(maxsize=None)
def preprocess_radical(n):
    global radical
    radical = [1] * (n + 1)
    
    for i in range(2, n + 1):
        x = i
        min_prime = primes[min_prime_index[x]]
        while x % min_prime == 0:
            x //= min_prime
        radical[i] = radical[x] * min_prime


def get_radical_sorted_list(n):
    return sorted(list(range(1, n + 1)), key=lambda x: (radical[x], x))


N = -1


def _brute_force_ab_failed():
    """
        'ab' can be very large, so the enumeration here is not enough
    """
    global N
    N = 1000
    # N = 120000
    
    preprocess_primes(int(1e6))
    preprocess_radical(N)
    radical_sorted_list = get_radical_sorted_list(N)
    
    print(radical_sorted_list[:10])
    abc_hit_tuple_count = 0
    c_set = set()
    for c in range(3, N):
        for ab in radical_sorted_list:
            if gcd(ab, c) != 1:
                continue
            if radical[ab] * radical[c] >= c:
                break
            a_b_square = c ** 2 - 4 * ab
            if a_b_square <= 0:
                continue
            a_b = int(sqrt(a_b_square))
            if a_b ** 2 != a_b_square:
                continue
            if (a_b + c) % 2 == 1:
                continue
            b = (a_b + c) // 2
            a = c - b
            c_set.add(c)
            print(f'found an abc-hit tuple ({a}, {b}, {c})')
            abc_hit_tuple_count += 1
    print(f'total abc-hit tuples: {abc_hit_tuple_count}, answer: {sum(c_set)}')


abc_hit_tuple_set = set()


def dfs(p_index, a, b, rad_ab):
    if a + b >= N or rad_ab >= N:
        return
    
    def test_abc_hit_tuple():
        # test a, b, a+b, tuple
        if a >= b:
            return
        c = a + b
        if (a, b, c) in abc_hit_tuple_set:
            # print(f'warning: abc-hit tuple already exists: ({a}, {b}, {c})')
            return
        if rad_ab * radical[c] >= c:
            return
        print(f'found an abc-hit tuple ({a}, {b}, {c})')
        abc_hit_tuple_set.add((a, b, c))
        return
    
    test_abc_hit_tuple()
    
    prime = primes[p_index]
    if ((a * prime + b >= N and a + b * prime >= N) or rad_ab * prime >= N):  # cannot add more primes
        return
    
    dfs(p_index + 1, a, b, rad_ab)
    
    _rad_ab = rad_ab * prime
    _a = a
    while True:
        _a = _a * prime
        if _a + b >= N:
            break
        dfs(p_index + 1, _a, b, _rad_ab)
    _b = b
    while True:
        _b = _b * prime
        if a + _b >= N:
            break
        dfs(p_index + 1, a, _b, _rad_ab)
        

def brute_force_dfs():
    global N
    N = 1000
    # N = 120000  # tostal abc-hit tuples: 456, answer: 18407904
     
    preprocess_primes(int(1e6))
    preprocess_radical(N)
    dfs(0, 1, 1, 1)
    answer = sum([x[2] for x in abc_hit_tuple_set])
    print(f'total abc-hit tuples: {len(abc_hit_tuple_set)}, answer: {answer}')
    
    
if __name__ == '__main__':
    brute_force_dfs()
    pass
