from functools import lru_cache

M = 3

@lru_cache(maxsize=None)
def dp(n):
    if n < M:
        return 1
    answer = dp(n - 1) + sum(dp(n - m - 1) for m in range(M, n)) + (dp(0) if n >= M else 0)
    return answer


if __name__ == '__main__':
    print(dp(50))
    pass
