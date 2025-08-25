from math import sqrt

def lower_bound(l, r, x):
    while l < r:
        mid = (l + r + 1) // 2
        if mid * mid <= x: 
            l = mid
        else:
            r = mid - 1
    return l
    
def cal(x):
    return sum([int(c) for c in str(x)])
    
def get(x):
    return cal(lower_bound(10**99, 10**99*x, 10**198*x))
    
def run():  
    # print(lower_bound(10**99, 10**99*2, 10**198*2))
    res = 0
    for i in range(100):
        if int(sqrt(i))**2 != i:
            r = get(i)
            res += r
            print('%d: %d' % (i, r))
    print(res)
        
run()
        
