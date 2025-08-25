def chk(x):
    for i in range(50):
        x = x + int(str(x)[::-1])
        if str(x) == str(x)[::-1]:
            return False
    return True
    
sum = 0
for i in range(1, 10000):
    sum += chk(i)
print(sum)
