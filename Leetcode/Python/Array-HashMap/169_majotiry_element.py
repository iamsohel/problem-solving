class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsDict = {}
        for i in nums:
            if i in numsDict:
                numsDict[i] += 1
            else:
                numsDict[i] = 1
        for key, value in numsDict.items():
            if value > (len(nums) / 2):
                return key
