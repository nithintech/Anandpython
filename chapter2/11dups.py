lis=[1,1,1,1,1,4,1,2,2,3,3]
def dups(lis):
	new=[]
	for i in lis:
		lis=lis[1:]
		if i in lis:
			if i not in new:
				new.append(i)

	print new
dups(lis)

