from math import sqrt
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
def get_factor_number(n, power=1):
    if n == 0:
        return 0
    if n == 1:
        return 1
    prime_index = min_prime_index[n]
    prime_count = 0
    while min_prime_index[n] == prime_index:
        n //= primes[prime_index]
        prime_count += power
    return get_factor_number(n, power) * (prime_count + 1)


@lru_cache(maxsize=None)
def simple_check_prime(p):
    if p < 2:
        return False
    
    if p < len(is_prime):
        return is_prime[p]
    
    # simple optimization for large prime
    p_str = str(p)
    if sum([int(c) for c in p_str]) % 3 == 0:
        return False
    if p_str[-1] in ['0', '2', '4', '5', '6', '8']:
        return False
    
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    
    return True


def get_distinct_solution_number(n):
    return (get_factor_number(n, 2) + 1) >> 1


if __name__ == '__main__':
    preprocess_primes(int(1e7))
    max_answer = 0
    for i in range(0, int(1e7) + 1):
        result = get_distinct_solution_number(i)
        if result > 1000:
            print(f'get {result} solutions for {i}, which is the first to exceed 1000')
            break
    pass
