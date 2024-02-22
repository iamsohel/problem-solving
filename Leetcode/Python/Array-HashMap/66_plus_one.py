def plus_one(digits):
    large_digit = ''
    for i in digits:
        large_digit += str(i)
    large_digit = int(large_digit) + 1
    print(large_digit)
    return [int(i) for i in str(large_digit)]


a = plus_one([1, 2, 3])
print(a)
