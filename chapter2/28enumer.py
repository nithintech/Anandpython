def enumer(x):
	m=zip(x,range(1,len(x)+1))
	print m
 	for k,v in m:
		print k,v
	#return [(x[i],m[j]) for x[i] in x for m[j] in m if i==j]
	
enumer(['a','b','c','d'])
