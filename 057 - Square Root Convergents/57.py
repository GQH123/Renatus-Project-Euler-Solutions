
a = 1
b = 2

ans = 0
for i in range(1000):
    ans += len(str(a + b)) > len(str(b))
    c = (b << 1) + a
    a = b
    b = c
    
print(ans)
