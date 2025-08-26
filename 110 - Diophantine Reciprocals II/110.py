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


def test_maximum_factorization():
    """
        max_answer: 1, i: 1
        max_answer: 2, i: 2
        max_answer: 3, i: 4
        max_answer: 5, i: 6
        max_answer: 8, i: 12
        max_answer: 11, i: 24
        max_answer: 14, i: 30
        max_answer: 23, i: 60
        max_answer: 32, i: 120
        max_answer: 38, i: 180
        max_answer: 41, i: 210
        max_answer: 53, i: 360
        max_answer: 68, i: 420
        max_answer: 95, i: 840
        max_answer: 113, i: 1260
        max_answer: 122, i: 1680
        max_answer: 158, i: 2520
        max_answer: 203, i: 4620
        max_answer: 221, i: 7560
        max_answer: 284, i: 9240
        max_answer: 338, i: 13860
        max_answer: 365, i: 18480
        max_answer: 473, i: 27720
        max_answer: 608, i: 55440
        max_answer: 662, i: 83160
        max_answer: 743, i: 110880
        max_answer: 851, i: 120120
        max_answer: 1013, i: 180180
        max_answer: 1094, i: 240240
        max_answer: 1418, i: 360360
        max_answer: 1823, i: 720720
        max_answer: 1985, i: 1081080
        max_answer: 2228, i: 1441440
        max_answer: 2363, i: 1801800
        max_answer: 2552, i: 2042040
        max_answer: 2633, i: 2882880
        max_answer: 3038, i: 3063060
        max_answer: 3281, i: 4084080
        max_answer: 3308, i: 5405400
        max_answer: 4253, i: 6126120
    """
    preprocess_primes(int(1e7))
    max_answer = 0
    for i in range(0, int(1e7) + 1):
        result = get_distinct_solution_number(i)
        if result > max_answer:
            max_answer = result
            print(f'max_answer: {max_answer}, i: {i}')


N = -1
M = int(4e6)
minimum_n = -1
minimum_n_answer = -1


def factorization_dfs(n, last_exponent, current_answer, current_minimum_n):
    # print(f'n: {n}, current_answer: {current_answer}, current_minimum_n: {current_minimum_n}')
    """
    update minimum_n: 222844766188344300, current_answer: 5695313
    update minimum_n: 52331045326680120, current_answer: 5580131
    update minimum_n: 18255015811632600, current_answer: 5166788
    update minimum_n: 10953009486979560, current_answer: 4340102
    update minimum_n: 9350130049860600, current_answer: 4018613
    """
    real_answer = (current_answer + 1) // 2
    if real_answer > M:
        global minimum_n, minimum_n_answer
        if minimum_n == -1 or current_minimum_n < minimum_n:
            print(f'update minimum_n: {current_minimum_n}, current_answer: {real_answer}')
            minimum_n = current_minimum_n
            minimum_n_answer = real_answer
        return
    
    if minimum_n != -1 and current_minimum_n > minimum_n:
        return
    
    if n == N:
        return

    base = primes[n]
    exponent = 0
    next_minimum_n = current_minimum_n
    while True:
        if last_exponent != -1 and exponent > last_exponent:
            break
        next_answer = current_answer * (exponent*2 + 1)
        factorization_dfs(n + 1, exponent, next_answer, next_minimum_n)
        if next_answer > M:
            break
        next_minimum_n *= base
        exponent += 1


def brute_force_factorization():  # at most 15 primes because 3^15 > 8*1e6-1
    global N
    N = 15
    factorization_dfs(0, -1, 1, 1)


if __name__ == '__main__':
    preprocess_primes(int(1e7))
    brute_force_factorization()
    pass