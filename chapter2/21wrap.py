f=open("1.txt",'r')
new=[]
new1=[]
def wrap(f):
	for d in f:
		t=len(d)
		p=t/10		
		m=[]
		w=10
		for i in d:
			m.append(i)
		j=0
		while j<p+1:
			new.append(m[:10])
			m=m[10:]	
			j=j+1
	for i in new:
		 q= "".join(i)
                 print q

								
wrap(f)
