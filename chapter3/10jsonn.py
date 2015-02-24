import urllib
import json
def ip1():
	myip=json.load(urllib.urlopen('http://httpbin.org/ip'))
	print myip
ip1()
