from math import sqrt
from functools import lru_cache
from gmpy2 import get_context, isqrt  # , cos, const_pi, sqrt, floor, ...


def set_gmpy2_context(precision=1000, allow_complex=True):
    ctx = get_context()
    ctx.precision = precision
    ctx.allow_complex = allow_complex


def check_square_number(x):
    return isqrt(x)**2 == x


combinations = []


def preprocess_combinations(n=100):  # calculate all combinations C(i, j) in range [0, n]
    global combinations
    combinations = [[0] * (n + 1) for _ in range(n + 1)]
    combinations[0][0] = 1
    for i in range(1, n + 1):
        combinations[i][0] = 1
        for j in range(1, i):
            combinations[i][j] = combinations[i-1][j-1] + combinations[i-1][j]
        combinations[i][i] = 1


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


radical = []


@lru_cache(maxsize=None)
def preprocess_radical(n):
    global radical
    radical = [1] * (n + 1)
    
    for i in range(2, n + 1):
        x = i
        min_prime = primes[min_prime_index[x]]
        while x % min_prime == 0:
            x //= min_prime
        radical[i] = radical[x] * min_prime


def get_radical_sorted_list(n):
    return sorted(list(range(1, n + 1)), key=lambda x: (radical[x], x))


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


@lru_cache(maxsize=None)
def simple_check_prime(p):
    if p < 2:
        return False
    
    if p < len(is_prime):
        return is_prime[p]
    
    # simple optimization for large primes
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


def fast_power_mod(x, y, mod):
    result = 1
    while y > 0:
        if (y & 1) == 1:
            result = (result * x) % mod
        x = (x * x) % mod
        y >>= 1
    return result


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


def check_palindrome_number(x):
    return str(x) == str(x)[::-1]


if __name__ == '__main__':
    pass
