from math import sqrt

def isSqu(x):
    i = int(sqrt(x))
    return i**2 == x

M = 1
ans = 0
while True:
    M += 1
    for i in range(2, (M << 1 | 1)):
        if isSqu(i**2+M**2):
            ans += ((M+1-abs(i-(M+1)))//2)
    print('%d: %d' % (M, ans))
    if (ans > 1000000):
        break
