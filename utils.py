from math import sqrt
from functools import lru_cache


def preprocess_combination_coefficients(n=100):
    """
        Preprocess the combination coefficients for the binomial theorem.
    """
    combination_coefficients = [[0] * n for _ in range(n)]
    combination_coefficients[0][0] = 1
    for i in range(1, n):
        combination_coefficients[i][0] = 1
        for j in range(1, i):
            combination_coefficients[i][j] = combination_coefficients[i-1][j-1] + combination_coefficients[i-1][j]
        combination_coefficients[i][i] = 1
    return combination_coefficients


combination_coefficients = preprocess_combination_coefficients()


def get_combination_coefficients(n, k):
    return combination_coefficients[n][k]


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
def simple_check_prime(p):
    if p < 2:
        return False
    
    if p < len(is_prime):
        return is_prime[p]
    
    # simple optimization for large prime
    if p > int(1e7):
        p_str = str(p)
        if sum([int(c) for c in p_str]) % 3 == 0:
            return False
        if p_str[-1] in ['0', '2', '4', '5', '6', '8']:
            return False
    
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    
    return True


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


def lowbit(x):
    return x & -x


bitmasks = []


def preprocess_bitmasks(n):
    global bitmasks
    bitmasks = [[] for _ in range(n+1)]
    for i in range(0, 1 << n):
        bitmasks[i.bit_count()].append(i)
    for _bitmasks in bitmasks:
        _bitmasks.sort()


factorials = []


def preprocess_factorials(n=20):
    global factorials
    factorials = [1] * (n + 1)
    for i in range(2, n + 1):
        factorials[i] = factorials[i - 1] * i


def get_permutation(digits, index):
    if not digits:
        return []
    current_digit_index = index // factorials[len(digits) - 1]
    return [digits[current_digit_index]] + get_permutation(digits[:current_digit_index] + digits[current_digit_index + 1:], index % factorials[len(digits) - 1])


def get_permutation_string(digits, index):
    if not digits:
        return ''
    current_digit_index = index // factorials[len(digits) - 1]
    return digits[current_digit_index] + get_permutation_string(digits[:current_digit_index] + digits[current_digit_index + 1:], index % factorials[len(digits) - 1])


if __name__ == '__main__':
    pass
