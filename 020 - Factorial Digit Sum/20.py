from math import *

x = factorial(100)
ans = 0
while x > 0: 
	ans += x % 10
	x //= 10
print(ans)
