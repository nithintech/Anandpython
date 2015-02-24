lis=["python","scala","haskell","ruby","c","perl"]
def lensort(lis):
	lis.sort(key=lambda x:len(x))
	print lis
lensort(lis)

