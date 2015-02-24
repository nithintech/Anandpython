import re
import os
def findpython(lis):
  n=0
  for i in lis:
    lis=os.listdir(i)
    for j in lis:
      match=re.search('.py',j)
      if match:
        n += 1
      if os.path.isdir(i+'/'+j):
        yield i+'/'+j
  print '(.py)','---->',n


def fun(a):
  return (k for k in a)


lis=['/home/us/nithinpython/']          
b=findpython(lis)


w=fun(b)
for i in w:
  lis.append(i)

