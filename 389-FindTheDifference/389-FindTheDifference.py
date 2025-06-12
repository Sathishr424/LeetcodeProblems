# Last updated: 12/6/2025, 5:49:57 am
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash = defaultdict(int)
        for val in s:
            hash[val] += 1
        for val in t:
            if hash[val] == 0:
                return val
            hash[val] -= 1