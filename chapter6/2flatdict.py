b={}
def flat_dict(a,res=None):
	if res is None:
		res={}
	for x in a:
		if isinstance(a[x],dict):
			for j in a[x]:
				b[x+'.'+j]=a[x][j]
	    			flat_dict(b,res)
		else:
			res[x]=a[x]
	return res
print flat_dict({'a':1,'b':{'c':3,'d':4},'e':5})
