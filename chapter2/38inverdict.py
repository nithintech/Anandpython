def invert(dic):
  for key,value in dic.items():
    del dic[key]
    dic[value]=key
  print dic
invert({'r':4,'t':2,'u':5})
