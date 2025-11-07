# Problem 123. Prime Square Remainders
# Link: https://projecteuler.net/problem=123
# Answer: 21035
# Language: Python
# Author: Renatus
# Date: 2025-08-29 12:09:17

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


def main():
    preprocess_primes(int(1e7))
    for i, prime in enumerate(primes[::2]):
        n = 2 * i + 1
        if 2 * n * prime > int(1e10):
            print(f'the remainder of the {2*i+1}-th prime {prime} first exceeds 10^10')
            return
    print('no prime square remainder exceeds 10^10')


if __name__ == '__main__':
    main()
    pass
