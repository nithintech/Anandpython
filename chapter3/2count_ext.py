import os
import sys
a=[]
b=[]
sys.argv[1]
def files():
	for fl in os.walk(sys.argv[1]):
		print fl
	f=fl[-1]
	#print f
	for i in f:
		a.append(i.split('.'))
	#print a	
	for i in a:	
		b.append(i[1])
	#print b
	f={}
	for w in b:
		f[w]=f.get(w,0)+1
	#print f
	for k,v in f.items():
		print k,v
		#m.append(fl.split("."))
		
files()
