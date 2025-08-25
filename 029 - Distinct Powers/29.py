lis = []
for a in range(2, 101):
	for b in range(2, 101):
		x = a**b
		lis.append(x)
print(len(set(lis)))
