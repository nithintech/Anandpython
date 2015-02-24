def triple(x):
	return [(a,b,c) for a in range(1,x) for b in range(a,x) for c in range(1,x) if a+b==c]
print triple(6)

