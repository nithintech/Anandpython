x=["a.c","b.txt","c.py","d.txt","f.py","g.c"]
a=[]
f=[]
def extsort(x):
        for i in x:
                a.append(i.split("."))
        print a
        k=sorted(a,key=lambda x:x[1])
        print k
        for i in k:
                f.append(".".join(i))
	print "sorted list:"
        print f
extsort(x)

