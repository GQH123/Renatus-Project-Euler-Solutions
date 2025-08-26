from functools import lru_cache

M = 50

@lru_cache(maxsize=None)
def dp(n):
    if n < M:
        return 1
    answer = dp(n - 1) + sum(dp(n - m - 1) for m in range(M, n)) + (dp(0) if n >= M else 0)
    return answer


if __name__ == '__main__':
    n = 1
    while True:
        dp_n = dp(n)
        print(f'n = {n}, dp(n) = {dp_n}', flush=True)
        if dp_n > 1000000:
            break
        n += 1
    pass
