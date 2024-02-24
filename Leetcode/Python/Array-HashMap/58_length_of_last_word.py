class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        removeSpaceFromBothSide = s.strip()
        splitS = removeSpaceFromBothSide.split(" ")
        return len(splitS[-1])
