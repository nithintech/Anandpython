def map(fn,b):
	return [fn(i) for i in b]
def cube(a):
	print a*a*a
map(cube,range(10))

