import numpy as np
from timeit import default_timer as timer

# a = np.array([1, 2, 3])
# print(a)
# print(a.shape)
# print(a.dtype)
# print(a.ndim)
# print(a.size)
# print(a.itemsize)
# print(a[0])
# a[0] = 10
# print(a)
# b = a * np.array([2, 0, 2])
# print(b)

l = [1, 2, 3]
a = np.array([1, 2, 3])

# l = l + [4]
# a = a + np.array([4])
# l = l * 2
# a = a * 2
a = np.sqrt(a)
# print(l)
# print(a)

# Dot products
l1 = [1, 2, 3]
l2 = [4, 5, 6]
a1 = np.array(l1)
a2 = np.array(l2)
dot = 0
dot = np.dot(a1, a2)
# print(dot)

sum1 = a1 * a2
dot = (a1 * a2).sum()
# print(dot)
dot = a1 @ a2
# print(dot)

# performance test [speed test array vs list]
a = np.random.randn(1000)
b = np.random.randn(1000)
A = list(a)
B = list(b)
T = 1000


def dot1():
    dot = 0
    for i in range(len(A)):
        dot += A[i] * B[i]
    return dot


def dot2():
    return np.dot(a, b)


start = timer()
for i in range(T):
    dot1()
end = timer()
t1 = end - start

start = timer()
for i in range(T):
    dot2()
end = timer()

t2 = end - start

# print("time with list: ", t1)
# print("time with array: ", t2)
# print('Ratio', t1/t2)


# multidimensional array

m = np.array([[1, 2], [3, 4]])
print(m)
print(m.shape)
print(m[0])
print(m[0][0])
print(m[0, 0])

# slicing
