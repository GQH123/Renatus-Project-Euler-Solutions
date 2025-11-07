# Problem 141. Square Progressive Numbers
# Link: https://projecteuler.net/problem=141
# Answer: 878454337159
# Language: Python
# Author: Renatus
# Date: 2025-08-30 16:03:52

from functools import lru_cache
from tqdm import tqdm
from gmpy2 import isqrt, mpz, get_context


def check_square_number(x):
    return isqrt(x)**2 == x


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


def get_square_less_half_divisors(x, sort=False):

    less_half_divisors = []
    x_prime_factorization = []
    
    _x = x
    while x > 1:
        exponent = 0
        prime = primes[min_prime_index[x]]
        while x % prime == 0:
            x //= prime
            exponent += 2  # x^2
        x_prime_factorization.append((prime, exponent))
    x = _x
    
    def dfs_get_divisors(d, p_index):
        if d >= x:  # less-half divisors of x^2
            return
        if p_index == len(x_prime_factorization):
            nonlocal less_half_divisors
            less_half_divisors.append(d)
            return
        prime, exponent = x_prime_factorization[p_index]
        for i in range(exponent + 1):
            dfs_get_divisors(d, p_index + 1)
            d *= prime
    
    dfs_get_divisors(1, 0)
        
    if sort:
        less_half_divisors = sorted(less_half_divisors)
    return less_half_divisors


def enumerate_b():
    """
        b^2 = ac, b < sqrt(1e12) = 1e6
    """
    ctx = get_context()
    ctx.precision = 1000
    ctx.allow_complex = True
    preprocess_primes(int(1e6))
    N = 1e12
    answer = set()
    for b in tqdm(range(1, isqrt(mpz(N)))):
        v = b ** 2
        for a in get_square_less_half_divisors(b):
            # assert v % a == 0 and a < b
            c = v // a
            n = a + b * c
            if n >= N:
                continue
            if check_square_number(n):
                answer.add(n)
    print(sum(answer))


if __name__ == '__main__':
    enumerate_b()
    pass
