from math import sqrt
from functools import lru_cache
from tqdm import tqdm

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
    if p > int(1e10):
        p_str = str(p)
        if sum([int(c) for c in p_str]) % 3 == 0:
            return False
        if p_str[-1] in ['0', '2', '4', '5', '6', '8']:
            return False
    
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    
    return True


factorials = []


def preprocess_factorials(n=20):
    global factorials
    factorials = [1] * (n + 1)
    for i in range(2, n + 1):
        factorials[i] = factorials[i - 1] * i


def get_permutation(digits, index):
    if not digits:
        return ''
    current_digit_index = index // factorials[len(digits) - 1]
    return digits[current_digit_index] + get_permutation(digits[:current_digit_index] + digits[current_digit_index + 1:], index % factorials[len(digits) - 1])


current_permutation = ''


@lru_cache(maxsize=None)
def dp(n, last_n=-1):
    if n == len(current_permutation):
        return 1
    answer = 0
    for next_n in range(n + 1, len(current_permutation)+1):
        x = int(current_permutation[n:next_n])
        if (last_n != -1 and x <= int(current_permutation[last_n:n])) or not simple_check_prime(x):
            continue
        answer += dp(next_n, n)
    return answer


if __name__ == '__main__':
    preprocess_primes(int(1e7))
    preprocess_factorials(9)
    answer = 0
    for i in tqdm(range(0, factorials[9])):
        current_permutation = get_permutation('123456789', i)
        answer += dp(0, -1)
        dp.cache_clear()
    print(answer)
    pass
