from math import *

cnt = 0
for i in range(1, 101): 
	for j in range(0, i + 1): 
		if factorial(i) / factorial(j) / factorial(i - j) > 1e6: 
			cnt += 1
			
print(cnt)
