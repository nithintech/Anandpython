import re
import urllib
x=[]
def links(url):
	f=urllib.urlopen(url)
	print f.readlines()
	x=re.findall('https:(\w+)',f)
	print x
links('http://docs.python.org/tutorial/interpreter.html')
