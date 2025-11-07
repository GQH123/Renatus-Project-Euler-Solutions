# Problem 142. Perfect Square Collection
# Link: https://projecteuler.net/problem=142
# Answer: 1006193
# Language: Python
# Author: Renatus
# Date: 2025-08-30 16:43:34

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


def enumerate_s():
    """
        x + y = a^2
        x + z = b^2
        y + z = c^2
        
        a > b > c > 0

        x - y = b^2 - c^2 = s^2
        y - z = a^2 - b^2 = t^2
        x - z = a^2 - c^2 = u^2 = s^2 + t^2
        
        s^2 = b^2 - c^2 = (b - c)(b + c) = u^2 - t^2 = (u - t)(u + t)
        
        z = \frac{b^2 + c^2 - a^2}{2} = \frac{b^2 - u^2}{2} > 0, b > u
        
        enumerate pairs of less than half divisors of s^2 and check if a^2 = c^2 + u^2 satisfies
    """
    ctx = get_context()
    ctx.precision = 1000
    ctx.allow_complex = True
    preprocess_primes(int(1e6))
    N = 1e6
    answer = -1
    for s in tqdm(range(1, isqrt(mpz(N)))):
        v = s ** 2
        less_half_divisors = get_square_less_half_divisors(s, sort=True)
        for bc_i in range(len(less_half_divisors)):
            b_sub_c = less_half_divisors[bc_i]
            b_add_c = v // b_sub_c
            if (b_sub_c + b_add_c) & 1:
                continue
            b = (b_sub_c + b_add_c) // 2
            c = b_add_c - b
            for ut_i in range(bc_i + 1, len(less_half_divisors)):
                u_sub_t = less_half_divisors[ut_i]
                u_add_t = v // u_sub_t
                if (u_sub_t + u_add_t) & 1:
                    continue
                u = (u_sub_t + u_add_t) // 2
                t = u_add_t - u
                assert b > u
                a_square = c**2 + u**2
                b_square = b**2
                c_square = c**2
                if (a_square + b_square + c_square) & 1:
                    continue
                if check_square_number(a_square):
                    a = isqrt(a_square)
                    x = (a_square + b_square - c_square) // 2
                    y = (a_square - b_square + c_square) // 2
                    z = (-a_square + b_square + c_square) // 2
                    print(f'found a={a}, b={b}, c={c}, u={u}, t={t}, s={s}, x={x}, y={y}, z={z}')
                    if answer == -1 or answer > x + y + z:
                        answer = x + y + z
    print(answer)


if __name__ == '__main__':
    enumerate_s()
    pass
