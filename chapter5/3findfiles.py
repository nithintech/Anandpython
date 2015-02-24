import os
import sys
lis=[]
def findfiles(f):
  
  for i in f:
    new=os.listdir(i)
    
    for j in new:
 
      if os.path.isdir(i+'/'+j):
        
        
        yield i+'/'+j
      else:
        print os.path.abspath(i+'/'+j)
def fun(a):

  return (j for j in a)
a=findfiles(sys.argv[1])
w=fun(a)

for k in w:
  
  lis.append(k)
