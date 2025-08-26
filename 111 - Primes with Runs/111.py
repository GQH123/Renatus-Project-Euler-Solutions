from math import sqrt
from functools import lru_cache


@lru_cache(maxsize=None)
def simple_check_prime(p):
    if p < 2:
        return False
    
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


def dfs_M(digits, n, d, left_d_number):
    if len(digits) == n:
        if left_d_number > 0:
            return False
        number = int(''.join(digits))
        if simple_check_prime(number):
            return True
        return False
    
    if left_d_number > n - len(digits):
        return False
    
    for i in range(1 if not digits else 0, 10):
        if i == d:
            if left_d_number > 0:
                if dfs_M(digits + [str(i)], n, d, left_d_number - 1):
                    return True
        else:
            if dfs_M(digits + [str(i)], n, d, left_d_number):
                return True


@lru_cache(maxsize=None)
def get_M(n, d):
    for left_d_number in range(n, 0, -1):
        if dfs_M([], n, d, left_d_number):
            return left_d_number
    return -1


def dfs_N(digits, n, d, left_d_number):
    if len(digits) == n:
        if left_d_number > 0:
            return 0
        number = int(''.join(digits))
        if simple_check_prime(number):
            return 1
        return 0
    
    if left_d_number > n - len(digits):
        return 0
    
    answer = 0
    for i in range(1 if not digits else 0, 10):
        if i == d:
            if left_d_number > 0:
                answer += dfs_N(digits + [str(i)], n, d, left_d_number - 1)
        else:
            answer += dfs_N(digits + [str(i)], n, d, left_d_number)
    return answer


@lru_cache(maxsize=None)
def get_N(n, d):
    M_n_d = get_M(n, d)
    return dfs_N([], n, d, M_n_d)


def dfs_S(digits, n, d, left_d_number):
    if len(digits) == n:
        if left_d_number > 0:
            return 0
        number = int(''.join(digits))
        if simple_check_prime(number):
            return number
        return 0
    
    if left_d_number > n - len(digits):
        return 0
    
    answer = 0
    for i in range(1 if not digits else 0, 10):
        if i == d:
            if left_d_number > 0:
                answer += dfs_S(digits + [str(i)], n, d, left_d_number - 1)
        else:
            answer += dfs_S(digits + [str(i)], n, d, left_d_number)
    return answer


@lru_cache(maxsize=None)
def get_S(n, d):
    M_n_d = get_M(n, d)
    return dfs_S([], n, d, M_n_d)


if __name__ == '__main__':
    answer = 0
    n = 10
    for d in range(10):
        answer += get_S(n, d)
        print(f'M({n}, {d}) = {get_M(n, d)}, N({n}, {d}) = {get_N(n, d)}, S({n}, {d}) = {get_S(n, d)}', flush=True)
    print(answer)
    pass
