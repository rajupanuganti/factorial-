from array import *

vals = array('i', [22, -4, 8, 98])

newArr=array(vals.typecode,(a*a for a in vals))
for e in newArr:
    print(e)