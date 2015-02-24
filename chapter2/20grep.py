def grep(fname,word):
	for i in open(fname):
		if word in i:
			print i
grep("/home/us/nithinpython/chapter2/foo.txt",'shanub') 
