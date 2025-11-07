from math import sqrt
from decimal import Decimal, getcontext


def d_pi():
    """Compute Pi to the current precision.

    >>> print(pi())
    3.141592653589793238462643383

    """
    getcontext().prec += 2  # extra digits for intermediate steps
    three = Decimal(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s               # unary plus applies the new precision


def d_exp(x):
    """Return e raised to the power of x.  Result type matches input type.

    >>> print(exp(Decimal(1)))
    2.718281828459045235360287471
    >>> print(exp(Decimal(2)))
    7.389056098930650227230427461
    >>> print(exp(2.0))
    7.38905609893
    >>> print(exp(2+0j))
    (7.38905609893+0j)

    """
    getcontext().prec += 2
    i, lasts, s, fact, num = 0, 0, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x
        s += num / fact
    getcontext().prec -= 2
    return +s


def d_cos(x):
    """Return the cosine of x as measured in radians.

    The Taylor series approximation works best for a small value of x.
    For larger values, first compute x = x % (2 * pi).

    >>> print(cos(Decimal('0.5')))
    0.8775825618903727161162815826
    >>> print(cos(0.5))
    0.87758256189
    >>> print(cos(0.5+0j))
    (0.87758256189+0j)

    """
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s


def d_sin(x):
    """Return the sine of x as measured in radians.

    The Taylor series approximation works best for a small value of x.
    For larger values, first compute x = x % (2 * pi).

    >>> print(sin(Decimal('0.5')))
    0.4794255386042030002732879352
    >>> print(sin(0.5))
    0.479425538604
    >>> print(sin(0.5+0j))
    (0.479425538604+0j)

    """
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s


def d_sinh(x):
    return (d_exp(x) - d_exp(-x)) / 2


def d_cosh(x):
    return (d_exp(x) + d_exp(-x)) / 2


def d_isin(ix):
    return complex(d_sin(ix.real) * d_cosh(ix.imag), d_cos(ix.real) * d_sinh(ix.imag))


def d_icos(ix):
    return complex(d_cos(ix.real) * d_cosh(ix.imag), -d_sin(ix.real) * d_sinh(ix.imag))


def d_isqrt(ix):
    r = (Decimal(ix.real) ** 2 + Decimal(ix.imag) ** 2).sqrt()


def simple_brute_force():
    min_distance = 1000**2
    min_distance_n = -1
    for i in range(-1000, 1001):
        if i >= 0 and int(sqrt(i)) ** 2 == i:
            continue
        f_v = cmath.cos(cmath.pi * cmath.sqrt(i)).real
        if i == -1000:
            print(f_v)
        i_v = math.floor(f_v)
        if abs(f_v - i_v) < min_distance:
            min_distance = abs(f_v - i_v)
            min_distance_n = i
        if abs(f_v - (i_v + 1)) < min_distance:
            min_distance = abs(f_v - (i_v + 1))
            min_distance_n = i
            
    print(f'{min_distance_n} leads to minimum distance {min_distance}')
    # 962 leads to minimum distance 0.0012828256154242546