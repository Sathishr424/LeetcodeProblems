# Last updated: 12/6/2025, 5:43:04 am
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        first = {
            "b": 0,
            "a": 0,
            "n": 0
        }

        second = {
            "l": 0,
            "o": 0
        }

        for char in text:
            if char in first: first[char] += 1
            elif char in second: second[char] += 1
        ret = float('inf')
        for char in first:
            ret = min(first[char], ret)
        for char in second:
            ret = min(second[char]//2, ret)
        return ret