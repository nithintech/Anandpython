a=[1,2,3,4]
b=[]
def cum_pro(a):
	j=1
	for i in a:
		j=j*i
		b.append(j)
	print b
cum_pro(a)
