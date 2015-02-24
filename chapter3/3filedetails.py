import os
import time
def filedata():
	list=os.listdir('/home/us/nithinpython/chapter3')
	for filename in list:
		leng=os.path.getsize(filename)
		time=os.path.getmtime(filename)
		print filename,leng,time
filedata()
	
