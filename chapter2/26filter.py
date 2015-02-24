def filter(f,a):
	print [x for x in a if x%2==0]
def even(x):
	return x%2==0
filter(even,range(20))
