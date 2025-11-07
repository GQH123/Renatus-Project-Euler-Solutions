# Problem 131. Prime Cube Partnership
# Link: https://projecteuler.net/problem=131
# Answer: 173
# Language: Python
# Author: Renatus
# Date: 2025-08-29 23:07:56

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


def enumerate_s_and_test_prime():
    """
        We can prove that (a, p) = (a^2, a+p) = 1, in this way we know a = s^3 and p = 3s^2 + 3s + 1, so we can enumerate s and test whether p is a prime.
    """
    N = int(1e6)
    count = 0
    preprocess_primes(N)
    for s in range(1, N):
        v = 3 * s**2 + 3 * s + 1
        if v > N:
            break
        if is_prime[v]:
            print(f'found a prime p = 3s^2 + 3s + 1 = {v} for s = {s}')
            count += 1
    print(f'total prime with this remarkable property: {count}')


if __name__ == '__main__':
    enumerate_s_and_test_prime()
    pass
