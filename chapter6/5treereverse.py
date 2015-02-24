def treerev(lis):
  res=[]
  lis.reverse()
  for i in lis:
    if isinstance(i,list):
      res.append(treerev(i))
    else:
      res.append(i)
  return res

  
k=treerev([[1, 2], [3, [4, 5]], 6])
print k
