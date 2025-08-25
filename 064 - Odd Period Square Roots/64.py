from math import gcd, sqrt

x = -1
cnt = set()
ans = 0
def f(a, b, c, d):
    # print(a, b, c, d)
    global cnt
    # (a * sqrt(b) + c) / d
    dd = gcd(a, gcd(c, d))
    a //= dd
    c //= dd
    d //= dd
    
    if (a, b, c, d) in cnt: 
        print(b, len(cnt))
        global ans
        ans += (len(cnt) & 1)
        cnt = set()
        return
    
    cnt.add((a, b, c, d))
    
    _a, _b, _c, _d = a * d, b, -c * d, a * a * b - c * c
    inte = int((_a * sqrt(_b) + _c) / _d)
    _c -= inte * _d
    
    f(_a, _b, _c, _d)
    
for i in range(10000 + 1):
    sqrti = int(sqrt(i))
    if sqrti * sqrti == i: continue
    f(1, i, -sqrti, 1)
    
print(ans)
    
