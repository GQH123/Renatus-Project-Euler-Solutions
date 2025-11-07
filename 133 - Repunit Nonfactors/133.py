# Problem 133. Repunit Nonfactors
# Link: https://projecteuler.net/problem=133
# Answer: 453647705
# Language: Python
# Author: Renatus
# Date: 2025-08-29 23:17:22

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


def get_ord_p_10():
    """
        For desired primes p > 5, we know that 10^(10^t) % p == 1, so ord_{p}(10) | 10^t, namely ord_{p}(10) contains only prime factor 2 and 5. We can enumerate every divisor d of phi(p) = p - 1 and test if 10^d % p == 1 to calculate the ord_{p}(10).
    """
    N = int(1e5)
    count = 0
    answer = 2 + 3 + 5
    preprocess_primes(N)
    for p in primes[3:]:  # p = 2, 3, 5 is not valid
        ord_p_10 = p
        phi_p = phi[p]
        for d in range(1, phi_p):
            if d * d > phi_p:
                break
            if phi_p % d == 0:
                if fast_power_mod(10, d, p) == 1:  # d < phi_p // d
                    ord_p_10 = d
                    break
                if fast_power_mod(10, phi_p // d, p) == 1:
                    ord_p_10 = min(ord_p_10, phi_p // d)
        _ord_p_10 = ord_p_10
        while ord_p_10 % 2 == 0:
            ord_p_10 //= 2
        while ord_p_10 % 5 == 0:
            ord_p_10 //= 5
        if ord_p_10 != 1:
            answer += p
            continue
        count += 1
        print(f'found {count}-th prime p = {p} with ord_{p}(10) = {_ord_p_10}, which can be a factor of R(10^k)')
    
    print(f'sum of all primes below 10^5 which will never be a factor of R(10^k): {answer}')
            

if __name__ == '__main__':
    get_ord_p_10()
    pass
