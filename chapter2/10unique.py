a=[1,1,3,2,4,2]
b=[]
def unq():
        for i in range(len(a)):
                if a[i] not in b:
                        b.append(a[i])
        print b
unq()

