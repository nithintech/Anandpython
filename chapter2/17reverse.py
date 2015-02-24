f=open("/home/us/nithinpython/chapter2/foo.txt")
new=f.readlines()
new=[i.strip() for i in new]
for i in reversed(new):
	print i
