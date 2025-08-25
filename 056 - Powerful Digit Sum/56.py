def dsum(x):
    x = str(x)
    ans = 0
    for c in x:
        ans += int(c)
    return ans
    
max_dsum = 0
max_pair = (-1, -1)
for i in range(1, 100):
    for j in range(1, 100):
        ans = dsum(i**j)
        if ans > max_dsum:
            max_dsum = ans
            max_pair = (i, j)

print(max_dsum, max_pair)
