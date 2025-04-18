# Last updated: 18/4/2025, 8:34:25 pm
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)

        def greater(l, r):
            while l < m and r < n and word1[l] == word2[r]:
                l += 1
                r += 1
            return r == len(word2) or (l < len(word1) and word1[l] > word2[r])
        
        ret = []
        l = 0
        r = 0
        while l < m and r < n:
            if greater(l, r):
                ret.append(word1[l])
                l += 1
            else:
                ret.append(word2[r])
                r += 1
        
        while l < m:
            ret.append(word1[l])
            l += 1
        while r < n:
            ret.append(word2[r])
            r += 1
        
        return ''.join(ret)