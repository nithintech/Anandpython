a=[1,2,3]
b=["a","b","c"]

def zips(a,b):
	print [(a[i],b[j])for i in range(len(a)) for j in range(len(b)) if i==j]
zips(a,b)
