# Problem 132. Large Repunit Factors
# Link: https://projecteuler.net/problem=132
# Answer: 843296
# Language: Python
# Author: Renatus
# Date: 2025-08-29 23:14:01

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


def brute_force_p():
    preprocess_primes(int(1e6))
    count = 0
    answer = 0
    for p in primes:
        if fast_power_mod(10, int(1e9), 9 * p) == 1:
            count += 1
            answer += p
            print(f'found {count}-th prime factor {p}')
            if count == 40:
                print('sum of the first 40 prime factors:', answer)
                break


if __name__ == '__main__':
    brute_force_p()
    pass
