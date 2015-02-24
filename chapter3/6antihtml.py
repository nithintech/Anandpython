import urllib
import sys
import re
def antihtml(url):
  
  urllib.urlretrieve(url,'az.txt')
  f=open('az.txt').readlines()
  print f
 
  for each in f:
    match=re.findall('(\w+)(\s)' , each)
  print match 
antihtml(sys.argv[1])
