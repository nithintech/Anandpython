x=[1,2,3,4]
c=[]
def reverse(x):
	for i in range(1,len(x)+1):
		c.append(x[len(x)-i])
	print c
reverse(x)
