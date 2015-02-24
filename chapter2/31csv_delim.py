f=open('parse1.txt').read().split()
res=[]
def delim(f):
	for i in f:
		t=i.split('!')
		res.append(t)
	print res
delim(f)
