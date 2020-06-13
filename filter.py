def is_even(n):
    return n%2==0

nums = [2,8,7,9,88]
evens = list(filter(is_even,nums))

print(evens)


