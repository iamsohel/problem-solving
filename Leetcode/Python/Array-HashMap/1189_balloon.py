class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter('balloon')
        result = len(text)
        for c in balloon:
            result = min(result, countText[c] // balloon[c])
        return result
