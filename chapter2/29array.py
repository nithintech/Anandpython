def array(a,b):
	list1=[["none"]*b for i in range(a)]
	print list1
	return list1
def arrayadd(r,c,n,list1):   #r=raw c=column n=number list1=array
	list1[r][c]=n
	print list1
array(2,3)
arrayadd(0,1,4,array(2,3))
