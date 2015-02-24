def treemap(a,b,):
  lis=[]
  
  for i in b:
    if isinstance(i,list):
      lis.append(treemap(a,i))
    else:
      lis.append(a(i))
  return lis
fl=treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
print fl  
  
