class Solution:
    def twoSum1(self, nums, target):  # O(n^2)
        n = len(nums)
        for i in range(n-1):
            for j in range(i + 1, n):
                if (nums[i] + nums[j] == target):
                    return [i, j]


c = Solution()
print(c.twoSum1([2, 7, 11, 15], 9))
