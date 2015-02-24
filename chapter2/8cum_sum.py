a=[1,2,3,4]
b=[]
def cum_sum(a):
	j=0
	for i in a:
		j=j+i
		b.append(j)
	print b
cum_sum(a)
