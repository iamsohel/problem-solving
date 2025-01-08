class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        for num in nums:
            if count == 0:
                ans = num
            if num == ans:
                count += 1
            else:
                count -= 1
        return ans


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numDict = {}
        for num in nums:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1

        sortedDict = sorted(numDict.items(), key=lambda kv: kv[1])
        return sortedDict[-1][0]


result = majorityElement([3, 3, 4, 4, 4, 5])
