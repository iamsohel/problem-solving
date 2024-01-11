class Solution:
    def containsDuplicate(self, nums):
        hashset = {}
        for i in nums:
            if (i in hashset):
                return True
            hashset[i] = i
        return False


c = Solution()
print(c.containsDuplicate([1, 2, 3, 1]))
