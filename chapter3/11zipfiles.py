import zipfile
def zipf(l):
	a=zipfile.ZipFile("my.zip",'w')
	for i in l:
		a.write(i)
zipf(["jsonn.py","phonenum.py"])
