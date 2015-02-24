def product(a,b):
	if b==1:
		return a
	else:
		return a+product(a,b-1)
res=product(2,10)
print res
