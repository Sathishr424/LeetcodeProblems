# Last updated: 12/6/2025, 5:33:26 am
class Solution:
    def maxSubstrings(self, word: str) -> int:
        n = len(word)
        indexes = [[] for _ in range(26)]
        for i, char in enumerate(word):
            indexes[ord(char) - 97].append(i)

        @cache
        def rec(index):
            if n-index < 4: return 0
            
            char = ord(word[index]) - 97
            right = bisect_left(indexes[char], index+3)
            ans = rec(index+1)
            if right < len(indexes[char]):
                return max(ans, rec(indexes[char][right] + 1) + 1)
            return ans
        

        return rec(0)
            