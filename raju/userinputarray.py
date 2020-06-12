from array import*
arr = array('i',[])
n = int(input('length of the array'))

for i in range(n):
    x = int(input('enter the  values'))
    arr.append(x)

print(arr)

vals = int(input('enter search  value '))
k = 0
for e in arr:
    if e==vals:
        print(k)
        break
    k+=1

print(arr.index(vals))