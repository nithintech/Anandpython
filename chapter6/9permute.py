def permute(lis1,lis2):
  x=len(lis1)
  y=len(lis2)
 
  if y==2:
    res.append(lis1[:-2]+[lis2[0]]+[lis2[1]])
    res.append(lis1[:-2]+[lis2[1]]+[lis2[0]])
    return

  for i in range(y):
    n=lis2[1:]
    permute(lis1,n)
    temp=lis2[y-i-1]
    lis2[y-i-1]=lis2[0]
    lis2[0]=temp
    lis1=lis1[:x-y]+lis2[:]
res=[]
permute([1,3,5,7,9],[2,4,6,8,10])  
print res
for i in res:
  print i
    
