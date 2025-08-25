n = int(input())

ser = []

for i in range(n):
    if i == 0:
        ser.append(2)
    elif i % 3 == 2:
        ser.append(2 * (i + 1) // 3)
    else:
        ser.append(1)
        
def digit_sum(x):
    return sum([int(d) for d in str(x)])

def f():
    a, b = 0, 1
    for x in ser[::-1]:
        a += b * x
        a, b = b, a
    a, b = b, a
    print('%d/%d: %d' % (a, b, digit_sum(a)))
    
f()
