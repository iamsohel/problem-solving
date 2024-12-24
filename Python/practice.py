def merge(nums1, nums2, m, n):
    nums1.extend(nums2)
    nums3 = []
    for i in range(m+n):
        if i != 0:
            nums3.append(i)

    return nums3


a = merge([1, 2, 3, 0, 0, 0], [2, 5, 6], 3, 3)
print(a)


def missing_nums(nums, lower, upper):
    list2 = {}
    for i in range(lower, upper+1):
        if i not in nums:
            list2.append(i)
    return list2


res = missing_nums([2, 5, 8], 1, 10)
print(res)
