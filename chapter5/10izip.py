def izip(a,b):
  for i in a:
    yield i,b[0]
    b=b[1:]
def fun(a):
  return (i for i in a)
q=izip(['a','s','d'],[1,2,3])
e=fun(q)
for i,j in e:
  print i,j

