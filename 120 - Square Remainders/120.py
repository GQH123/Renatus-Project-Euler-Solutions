answer = 0
for a in range(3, 1001):
    if a % 2 == 0:
        answer += a * (a - 2)
    else:
        answer += a * (a - 1)

print(answer)