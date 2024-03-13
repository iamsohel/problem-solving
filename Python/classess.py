import random


class Store:
    def __init__(self):
        self.map = set()

    def insert(self, val):
        self.map.add(val)

    def remove(self, index):
        self.map.remove(index)

    def getItem(self):
        return random.choice(list(self.map))


store = Store()
store.insert(1)
store.insert(2)
store.insert(3)
store.remove(1)
# print(store.getItem())


class Operation:
    def __init__(self, a, b):
        sum = a + b
        print("sum", sum)


a = int(input("a="))
b = int(input("b="))
op = Operation(a, b)
