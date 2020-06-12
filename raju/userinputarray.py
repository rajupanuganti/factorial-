from array import*
arr = array('i',[])
n = int(input('length of the array'))

for i in range(n):
    x = int(input('enter the  values'))
    arr.append(x)

print(arr)