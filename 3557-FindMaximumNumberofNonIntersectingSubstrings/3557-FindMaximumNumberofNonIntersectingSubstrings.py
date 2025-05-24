# Last updated: 24/5/2025, 10:31:15 pm
class Solution:
    def maxSubstrings(self, word: str) -> int:
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
        

        return rec(0)
            