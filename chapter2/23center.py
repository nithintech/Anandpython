f=open("foo.txt",'r')
def center(f):
	lis=f.readlines()
	k=0
	for i in lis:
		k=k+1
		res=(k*"  "+i)
		k=k-1
		print res
center(f)
