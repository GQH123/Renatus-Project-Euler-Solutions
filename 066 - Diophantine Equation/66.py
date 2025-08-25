from math import sqrt, gcd

"""
def isprime(x):
    for i in range(2, x):
        if i * i > x: break
        if x % i == 0: return False
    return True
 
def ttry(x, y, d):   
    return x * x == d * y * y + 1

def solve(d):
    if d != 2 and isprime(d):
        for k in range(1, 10000000):
            i = k**2
            x = i * d + 1
            y = int(sqrt((x * x - 1) // d))
            # assert y**2 == (x * x - 1)//d
            if ttry(x, y, d):
                return x, y
            x = i * d - 1
            y = int(sqrt((x * x - 1) // d))
            # assert y**2 == (x * x - 1)//d
            if ttry(x, y, d):
                return x, y
            x = i + 1
            y = int(sqrt((x * x - 1) // d))
            # assert y**2 == (x * x - 1)//d
            if ttry(x, y, d):
                return x, y
            x = i - 1
            if x * x < 1: continue
            y = int(sqrt((x * x - 1) // d))
            # assert y**2 == (x * x - 1)//d
            if ttry(x, y, d):
                return x, y
            x = 2 * i + 1
            y = int(sqrt((x * x - 1) // d))
            # assert y**2 == (x * x - 1)//d
            if ttry(x, y, d):
                return x, y
            x = 2 * d * i - 1
            y = int(sqrt((x * x - 1) // d))
            # assert y**2 == (x * x - 1)//d
            if ttry(x, y, d):
                return x, y
                
    else:
        return -1, -1
        for i in range(2, 10000000000):
            if (i * i - 1) % d != 0: continue
            y = (i * i - 1) // d
            _y = int(sqrt(y))
            
            if ttry(x=i, y=_y, d=d):
                return i, _y
"""

def check(x, y, d):   
    return x * x == d * y * y + 1

"""
def matmul(a, b):
    assert(len(a[0]) == len(b))
    c = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c
    
def solve(d):
    ct = 0
    trans = [[0, 1], [d-1, 2]]
    now = trans
    y, x = 0, 1
    while ct < 20:
        ct += 1
        y, x = matmul(trans, [[y], [x]])
        y, x = y[0], x[0] - y[0]
        dd = gcd(x, y)
        y //= dd
        x //= dd
        # now = matmul(now, trans)
        print(x, y)
        if check(x, y, d): 
            print('%d: (%d, %d), try: %d' % (d, x, y, ct))
            return x, y
"""


def solve(D):
    sqrtd = int(sqrt(D))
    _num, _dom = 1, 0
    num, dom = sqrtd, 1
    a, b, c, d = 1, D, -sqrtd, 1
    ct = 1
    while True:
        if check(x=num, y=dom, d=D): 
            print('%d: (%d, %d), try: %d' % (D, num, dom, ct))
            return num, dom
        ct += 1
        dd = gcd(a, gcd(c, d))
        a //= dd
        c //= dd
        d //= dd
        
        a, b, c, d = a * d, b, -c * d, a * a * b - c * c
        inte = int((a * sqrt(b) + c) / d)
        c -= inte * d
        
        num_, dom_ = _num + num * inte, _dom + dom * inte
        _num, _dom = num, dom
        num, dom = num_, dom_
                 
mx, mxd = 0, -1    
for d in range(2, 1000 + 1):
    _d = int(sqrt(d))
    if _d * _d == d: continue
    x, y = solve(d)
    if x > mx:
        mx = x
        mxd = d
    
print(mx, mxd)
