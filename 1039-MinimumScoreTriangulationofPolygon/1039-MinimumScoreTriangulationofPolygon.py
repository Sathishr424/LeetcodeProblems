# Last updated: 29/9/2025, 11:27:20 pm
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        @cache
        def rec(i, j):
            if j - i < 2: return 0
            ans = inf

            for k in range(i+1, j):
                v = values[i] * values[j] * values[k]
                ans = min(ans, v + rec(i, k) + rec(k, j))
            
            return ans
        
        return rec(0, n - 1)