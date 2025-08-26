from functools import lru_cache

M_red = 2


@lru_cache(maxsize=None)
def dp_red(n):
    if n < M_red:
        return 1
    return dp_red(n - 1) + dp_red(n - M_red)


M_green = 3


@lru_cache(maxsize=None)
def dp_green(n):
    if n < M_green:
        return 1
    return dp_green(n - 1) + dp_green(n - M_green)


M_blue = 4


@lru_cache(maxsize=None)
def dp_blue(n):
    if n < M_blue:
        return 1
    return dp_blue(n - 1) + dp_blue(n - M_blue)


if __name__ == '__main__':
    N = 50
    print(dp_red(N) + dp_green(N) + dp_blue(N) - 3)
    pass
