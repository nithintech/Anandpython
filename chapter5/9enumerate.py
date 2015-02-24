def enum(x):
	l=list(x)
	for i,j in zip(l,range(1,len(l)+1)):
		print i,j


enum(iter(["a","b","c"]))
