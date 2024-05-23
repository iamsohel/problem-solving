
# course = "Python programming"
# print(course.upper())
# print(course.lower())

# string = " python programming "
# print(string.strip())
# print(string.lstrip())
# print(string.rstrip())
# print(course.split(" "))
# print(",".join(course))
# print(course.find("pro"))  # return -1 if the value is not found.
# print(course.index("Py"))  # raises an exception if the value is not found.
# print(course.replace("Python", "node.js"))
# print(course.startswith("Node"))
# print(course.endswith("ing"))
# print(course.isupper())
# print(course.islower())
# print(course.count("m"))
# #

class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def work(self):
        return f"{self.name} is working"

    def get_salary(self):
        return f"{self.name} is getting salary {self.salary}"


class Manager(Employee):
    def __init__(self, name, id, salary, department):
        super().__init__(name, id, salary)
        self.department = department

    def work(self):
        return f"{self.name} is managing {self.department} department"


class Engineer(Employee):
    def __init__(self, name, id, salary, specialty):
        super().__init__(name, id, salary)
        self.specialty = specialty

    def work(self):
        return f"{self.name} has specialty on {self.specialty}"


manager = Manager("Sohel", 1, 1000, 'sales')
engineer = Engineer("Rana", 2, 2000, 'SW')


def employee_work(emp):
    print(emp.work())


employees = [manager, engineer]
for employee in employees:
    employee_work(employee)


class Store:
    def __init__(self) -> None:
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def remove(self, value):
        self.values.discard(value)

    def get_random(self):
        import random
        return random.choices(list(self.values))


store = Store()
store.add(1)
store.add(2)
store.remove(4)
# print(store.get_random())


# factorial, fibonacci, prime, binary search, merge sort, recursion


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))


def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**.5)+1):
        if n % 2 == 0:
            return False

    return True


# print(prime(12))
# print(factorial(5))


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high) // 2
        if (arr[mid] == target):
            return mid
        elif (arr[mid] < target):
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(binary_search([1, 2, 3, 4, 5], 4))


def quick_sort(arr):  # nlogn
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


print(quick_sort([2, 1, 5, 3, 6]))
