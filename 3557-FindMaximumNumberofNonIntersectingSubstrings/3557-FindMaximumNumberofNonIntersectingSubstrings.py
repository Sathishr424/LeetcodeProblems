# Last updated: 24/5/2025, 10:30:16 pm
class Solution:
    def maxSubstrings(self, word: str) -> int:
        # accccbacbc
        n = len(word)
        alp = [ord(char) - 97 for char in word]
        indexes = [[] for _ in range(26)]
        for i, char in enumerate(word):
            indexes[ord(char) - 97].append(i)

        @cache
        def rec(index):
            if n-index < 4: return 0
            
            char = alp[index]
            right = bisect_left(indexes[char], index+3)
            ans = rec(index+1)
            if right < len(indexes[char]):
                return max(ans, rec(indexes[char][right] + 1) + 1)
            return ans
        
        ret = 0
        for i in range(n):
            ret = max(ret, rec(i))

        return ret
            