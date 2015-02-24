import re
from inspect import isfunction
def mydoc(re):
	#get all entries of a module
	a=dir(re)
	for i in a:
		print i,i.__doc__
mydoc(re)
	
	
