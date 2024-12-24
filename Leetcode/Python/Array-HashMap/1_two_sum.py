class Solution:
    def twoSum1(self, nums, target):  # O(n^2)
        n = len(nums)
        for i in range(n-1):
            for j in range(i + 1, n):
                if (nums[i] + nums[j] == target):
                    return [i, j]

    def twoSum2(self, nums, target):  # O(n) time
        # O(n) space
        hashMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i


c = Solution()
print(c.twoSum1([2, 7, 11, 15], 9))


def missing_number(nums, lower, higher):
    missing_number = []
    for i in range(lower, higher+1):
        if i not in nums:
            missing_number.append(i)
    return missing_number
