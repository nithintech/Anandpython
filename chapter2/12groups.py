lis=[1,8,5,6,7,1,2,3,4,5]
lim=4
def group(lis,lim):
        leng=len(lis)
        res=[]
        while leng>0:
                newlis=[]
                k=0
                for i in lis:
                        if k>=lim:
                                break
                        newlis.append(i)
                        k=k+1
                res.append(newlis)
                lis=lis[lim:leng]
        return res
print group([1,8,5,6,7,1,2,3,4,5],3)
