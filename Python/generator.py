# generator object are iterable, just like list we can iterate over them
# and each iteration they generate a new value
# so unlike list they dont store value in memory, they generate new value in each iteration
# as they dont store the item in memory you wont get the total number of item
# so for large data set we should we generator object

values = (i*2 for i in range(5))  # genertor object
values2 = [i * 2 for i in range(5)]
print(values, values2)
for i in values:
    print(i)
