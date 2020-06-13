def count(list):
    even = 0
    odd = 0

    for i in list:
        if i % 2 == 0:
            even += 1

        else:
            odd += 1

    return even, odd


list = [24, 20, 14, 28, 29, 7, 5, 77]
even,odd = count(list)

print('Even:{} and Odd:{}'.format(even,odd))