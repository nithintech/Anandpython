new=[]
f=open('parse.txt').read().split()
#print f
def parse(f):
	for i in f:
		t=i.split(',')
		new.append(t)		
	print new
parse(f)

	
