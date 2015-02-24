lis=["python","java","Java","Python","haskell","HASkell","ruby"]
leng=len(lis)
m=range(len(lis))
new=[]
def strunique(lis):
	for i in m:
		lis[i]=lis[i].lower()
		if lis[i] not in new:
			new.append(lis[i])
	print new
strunique(lis)
	
