import string
def mutate(strng):
  w=[]
  leng=len(strng)
  old=strng
  t=leng
  b=leng
  let=string.ascii_lowercase
  w.append(strng)
  for i in range(0,leng):
    
    t=t-1
    new=old[:t]+old[t+1:]
    w.append(new)
    for i in let:
      al=old[:t]+i+old[t+1:]
      r=old[:b]+i+old[b:]
      w.append(al)
      w.append(r)
    b=b-1
  for j in range(leng-1):
    sw=old[:j]+old[j+1]+old[j]+old[j+2:]
    w.append(sw)
  
  return w
def nearly('net','netzzz'):
  word=mutate(b)
  return a in word    


