import os
import urllib
def wget(url):
	f=urllib.urlopen(url)
	if os.path.basename(url):
		name=os.path.basename(url)
	else:
		name="index.html"
	file=os.path.join('nettu',name)
	index=open(file,'r')
	for i in file:
		index.write(i)

print wget("http://docs.python.org/tutorial/interpreter.html")
