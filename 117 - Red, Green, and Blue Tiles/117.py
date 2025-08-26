from functools import lru_cache

M = [2, 3, 4]


@lru_cache(maxsize=None)
def dp(n):
    if n < M[0]:
        return 1
    return dp(n - 1) + sum(dp(n - m) for m in M if n >= m)


if __name__ == '__main__':
    N = 50
    print(dp(N))
    pass
