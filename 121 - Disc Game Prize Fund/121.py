from functools import lru_cache

N = -1


@lru_cache(maxsize=None)
def dp(pr, pb, br, bb, n):
    if bb < 0:
        return 0
    
    if n == N:
        assert pb + pr == N
        return float(pb > pr)
    
    # assert br + bb == 2
    answer = 0
    
    _pr = pr + 1
    _pb = pb
    # _dp = ((br + 1) * dp(_pr, _pb, br, bb, n + 1) + bb * dp(_pr, _pb, br + 1, bb - 1, n + 1)) / (br + bb + 1)
    # _dp = (br * dp(_pr, _pb, br, bb, n + 1) + bb * dp(_pr, _pb, br + 1, bb - 1, n + 1)) / (br + bb)
    _dp = dp(_pr, _pb, br + 1, bb, n + 1)  # after mulling over the problem for a while, it dawned on me that this is what it was really about.
    answer += br * _dp
    
    _pr = pr
    _pb = pb + 1
    # _dp = ((br + 1) * dp(_pr, _pb, br, bb, n + 1) + bb * dp(_pr, _pb, br + 1, bb - 1, n + 1)) / (br + bb + 1)
    # _dp = (br * dp(_pr, _pb, br, bb, n + 1) + bb * dp(_pr, _pb, br + 1, bb - 1, n + 1)) / (br + bb)
    _dp = dp(_pr, _pb, br + 1, bb, n + 1)
    answer += bb * _dp
    
    return answer / (br + bb)


if __name__ == '__main__':
    N = 15
    print(int(1 / dp(0, 0, 1, 1, 0)))
    pass