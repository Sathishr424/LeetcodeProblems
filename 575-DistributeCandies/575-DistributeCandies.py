# Last updated: 12/6/2025, 5:48:15 am
class Solution:
    def distributeCandies(self, c: List[int]) -> int:
        hash = {}
        n = len(c)
        ret = 0
        i = 0
        while i < n and ret < n//2:
            ret += c[i] not in hash
            hash[c[i]] = 1
            i += 1
        return ret