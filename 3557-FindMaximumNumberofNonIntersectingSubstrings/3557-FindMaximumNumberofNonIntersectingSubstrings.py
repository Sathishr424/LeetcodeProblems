# Last updated: 24/5/2025, 10:32:24 pm
class Solution:
    def maxSubstrings(self, word: str) -> int:
        n = len(word)
        indexes = [SortedList() for _ in range(26)]
        for i, char in enumerate(word):
            indexes[ord(char) - 97].add(i)

        @cache
        def rec(index):
            if n-index < 4: return 0
            
            char = ord(word[index]) - 97
            right = indexes[char].bisect_left(index+3)
            ans = rec(index+1)
            if right < len(indexes[char]):
                return max(ans, rec(indexes[char][right] + 1) + 1)
            return ans
        

        return rec(0)
            