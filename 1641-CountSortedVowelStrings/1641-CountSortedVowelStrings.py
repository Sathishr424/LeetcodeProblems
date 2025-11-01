# Last updated: 1/11/2025, 10:30:22 pm
class Solution:
    def countVowelStrings(self, n: int) -> int:

        @cache
        def rec(index, v_index):
            if index == n: return 1

            ans = 0
            for i in range(v_index, 5):
                ans += rec(index + 1, i)
            return ans
        
        return rec(0, 0)