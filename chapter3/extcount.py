import os
def file(dir):
	#print filenames
	fnames=os.listdir(dir)
	dict={}               #init__empty dic
	exten=[]		#init__empty list	
	for i in fnames:
		a=i.split('.')
		exten.append(a[1])
	for j in exten:
		dict[j]=dict.get(j,0)+1
	print dict
	for key,value in dict.items():print key,value
	
file('/home/us/nithinpython/chapter3')


