# Problem 137. Fibonacci Golden Nuggets
# Link: https://projecteuler.net/problem=137
# Answer: 1120149658760
# Language: Python
# Author: Renatus
# Date: 2025-08-30 01:02:52

import math
from functools import lru_cache


def solve():
    """
        (x^2 + x - 1)A_F(x) = -x, A_F(x) = -x / (x^2 + x - 1) = n, x = \frac{\sqrt{5n^2 + 2n + 1} - (n+1)}{2n}, so we need n such that 5n^2+2n+1 is a perfect square.
        
        However, this is a hard problem (general form of Pell's equation?), we can get a number sequence from OEIS (refer to https://oeis.org/A081018) which leads to correct answer, though I haven't figured out how this works.
        
        Answer: 1120149658760
    """
    ...


if __name__ == '__main__':
    solve()
    pass
