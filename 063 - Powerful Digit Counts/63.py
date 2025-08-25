ans = 0
for x in range(1, 10):
    for y in range(1, 1000):
        if len(str(x**y)) == y: ans += 1
print(ans)
