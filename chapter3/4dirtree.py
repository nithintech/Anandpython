import os
path=os.listdir('/home/us/nithin')
for each in path:	
	if os.path.isdir(each):
		print "+",each
		d=os.listdir(each)
		for j in d:
			print '|',6*'_',j
	else:print each
