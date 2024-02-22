def removeDuplicates(nums):
    # unique_list = []
    # underscore_list = []
    # for i in nums:
    #     if i in unique_list:
    #         underscore_list.append("_")
    #     else:
    #         unique_list.append(i)
    # changed_nums = f"nums= {unique_list + underscore_list}"
    # return len(unique_list)
    left = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[left] = nums[i]
            left += 1
    return left


print(removeDuplicates([1, 1, 2]))
