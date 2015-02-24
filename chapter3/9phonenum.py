import sys
import re
x=sys.argv[1]
def phone(x):
	if len(x)==10:
		match=re.findall('(\d)',x)
		if len(match)==10:
			print "phone num is valid"
		else:
			print "phone num invalid"
	else:
		print "phone num is invalid"
phone(x)
	
	
