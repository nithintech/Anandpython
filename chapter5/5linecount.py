import re
import os
def linecount(lis):
  n=0
  for i in lis:

    lis=os.listdir(i)
    for j in lis:
      match=re.search('.py',j)
      if match:
        d=open(j).readlines()
        n+=len(d)
        
      if os.path.isdir(i+'/'+j):

        yield i+'/'+j
  print n
def call(a):

  return (k for k in a)
lis=['/home/us/nithinpython/']
b=linecount(lis)
w=call(b)
for i in w:
  lis.append(i)
