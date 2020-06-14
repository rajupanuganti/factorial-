from functools import*
nums = [2,8,7, 6, 4,9]
evens = list(filter(lambda i : i%2==0,nums))

double = list(map(lambda i : i*2,nums))

sum = reduce(lambda a,b: a+b,double)

print(evens)
print(double)
print(sum)