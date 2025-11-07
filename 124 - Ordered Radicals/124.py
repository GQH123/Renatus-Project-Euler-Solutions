# Problem 124. Ordered Radicals
# Link: https://projecteuler.net/problem=124
# Answer: 21417
# Language: Python
# Author: Renatus
# Date: 2025-08-29 12:42:49

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


@lru_cache(maxsize=None)
def get_rad(x):
    if x == 1:
        return 1
    result = 1
    while x > 1:
        prime_index = min_prime_index[x]
        prime = primes[prime_index]
        result *= prime
        while x % prime == 0:
            x //= prime
    return result


def main():
    preprocess_primes(int(1e7))
    N = int(1e5)
    rad_sorted_list = sorted(list(range(1, N+1)), key=get_rad)
    print(rad_sorted_list[9999])


if __name__ == '__main__':
    main()
    pass
