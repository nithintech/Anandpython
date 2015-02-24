f=["1.txt","2.txt"]
for i in f:
	t=open(i)
	for i in t:
		if len(i)>40:
			print i

