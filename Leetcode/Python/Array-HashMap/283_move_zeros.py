class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
        return nums
