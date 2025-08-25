a = 1
b = 1
idx = 2
while True: 
	c = b
	b += a
	a = c
	idx += 1
	if len(str(b)) >= 1000: 
		break
print(idx)
