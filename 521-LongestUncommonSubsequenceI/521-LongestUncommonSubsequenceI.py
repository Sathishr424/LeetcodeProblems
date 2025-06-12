# Last updated: 12/6/2025, 5:48:37 am
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b: return -1
        return max(len(a), len(b))
        