from array import *

vals = array('i', [22, -4, 8, 98])

newArr=array(vals.typecode,(a for a in vals))
i=0
while i<len(newArr):
    print(newArr[i])
    i+=1