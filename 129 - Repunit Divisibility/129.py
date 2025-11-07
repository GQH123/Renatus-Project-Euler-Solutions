# Problem 129. Repunit Divisibility
# Link: https://projecteuler.net/problem=129
# Answer: 1000023
# Language: Python
# Author: Renatus
# Date: 2025-08-29 18:31:01

from math import gcd
from functools import lru_cache


def brute_force_A():
    # we can see that A(n) <= n, and in many cases A(n) = n - 1, so we can just start enumerating n from 1000000
    for n in range(1, 100):
        if gcd(n, 10) != 1:
            continue
        k = 1
        while True:
            if (10**k - 1) // 9 % n == 0:
                print(f'A({n}) = {k}')
                break
            k += 1


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


def brute_force_eumerate_n():
    preprocess_primes(int(1e7))
    n = 1000**2 + 1
    while n <= int(1e7):
        print(f'checking n = {n}')
        if gcd(n, 10) != 1:
            n += 1
            continue
        A_n = n * 3 if n % 3 == 0 else n
        phi_n = phi[n] * 3 if n % 3 == 0 else phi[n]
        failed = False
        for d in range(1, phi_n):
            if d * d > phi_n:
                break
            if phi_n % d != 0:
                continue
            
            f = d
            if fast_power_mod(10, f, 9 * n) == 1:
                A_n = min(A_n, f)
            if A_n <= 1000000:
                failed = True
                break
            
            f = phi_n // d
            if fast_power_mod(10, f, 9 * n) == 1:
                A_n = min(A_n, f)
            if A_n <= 1000000:
                failed = True
                break
        if not failed:
            print(f'found A({n}) = {A_n}, the first to exceed 1000000')
            break
        n += 1


def brute_force_eumerate_n_test():
    preprocess_primes(int(1e7))
    n = 1
    while n <= int(1e2):
        if gcd(n, 10) != 1:
            n += 1
            continue
        A_n = n * 3 if n % 3 == 0 else n
        phi_n = phi[n] * 3 if n % 3 == 0 else phi[n]
        for d in range(1, phi_n):
            if d * d > phi_n:
                break
            if phi_n % d != 0:
                continue
            
            f = d
            # print(f'f = {f}, mod = {fast_power_mod(10, f, 9 * n)}')
            if fast_power_mod(10, f, 9 * n) == 1:
                A_n = min(A_n, f)
            
            f = phi_n // d
            # print(f'f = {f}, mod = {fast_power_mod(10, f, 9 * n)}')
            if fast_power_mod(10, f, 9 * n) == 1:
                A_n = min(A_n, f)
        
        print(f'found A({n}) = {A_n}')
        n += 1
        # return

if __name__ == '__main__':
    # brute_force_A()
    # brute_force_eumerate_n_test()
    # preprocess_primes(int(1e7))
    # print(phi[:100])
    brute_force_eumerate_n()
    pass
