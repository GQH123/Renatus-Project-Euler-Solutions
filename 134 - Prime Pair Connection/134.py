# Problem 134. Prime Pair Connection
# Link: https://projecteuler.net/problem=134
# Answer: 18613426663617118
# Language: Python
# Author: Renatus
# Date: 2025-08-29 23:42:56

import math
from functools import lru_cache

min_prime_index = []
max_prime_index = []
is_prime = []
primes = []
phi = []


# Euler's Prime Sieve
def preprocess_primes(n=int(1e6)):  # sieve all primes in [1, n]
    global min_prime_index, max_prime_index, primes, is_prime, phi
    min_prime_index = [-1] * (n + 1)
    max_prime_index = [-1] * (n + 1)
    is_prime = [True] * (n + 1)
    phi = [0] * (n + 1)
    phi[1] = 1
    primes = []
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            min_prime_index[i] = len(primes) - 1
            max_prime_index[i] = len(primes) - 1
            phi[i] = i - 1
        for p_index, p in enumerate(primes):
            if i * p > n:
                break
            is_prime[i * p] = False
            min_prime_index[i * p] = p_index
            max_prime_index[i * p] = max_prime_index[i]
            if i % p == 0:
                phi[i * p] = phi[i] * p
                break
            else:
                phi[i * p] = phi[i] * (p - 1)


def fast_power_mod(x, y, mod):
    result = 1
    while y > 0:
        if (y & 1) == 1:
            result = (result * x) % mod
        x = (x * x) % mod
        y >>= 1
    return result


def fast_power_inverse(x, mod):
    return fast_power_mod(x, mod - 2, mod)


def traverse_prime_pairs():
    N = int(2e6)
    answer = 0
    preprocess_primes(N)
    for i, p1 in enumerate(primes[2:]):
        if p1 > int(1e6):
            break
        # p1, p2 = 19, 23
        p2 = primes[i + 3]
        coeff = 1
        _p1 = p1
        while _p1 > 0:
            coeff = coeff * 10
            _p1 //= 10
        s_head = (p2 - p1) * fast_power_inverse(coeff, p2) % p2
        s = s_head * coeff + p1
        # print(s)
        # return
        answer += s
    print(answer)

    
if __name__ == '__main__':
    traverse_prime_pairs()
    pass
