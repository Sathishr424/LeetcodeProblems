# Last updated: 12/6/2025, 5:46:12 am
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        prev = 0
        ret = []
        n = len(s)
        for i in range(1, n):
            if s[i] != s[i-1]:
                if i-prev >= 3:
                    ret.append([prev, i-1])
                prev = i
        if prev != n-1 and n-prev >= 3:
            ret.append([prev, n-1])

        return ret