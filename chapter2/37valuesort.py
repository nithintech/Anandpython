def val(dic):
  lis=[]
  res=[]
  for key,value in dic.items():
    lis.append((key,value))
  lis.sort()
  for i in lis:
    res.append(i[1])
  print res
val({'f':5,'w':7,'a':6})  
