# Last updated: 12/6/2025, 5:53:56 am
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word2)
        m = len(word1)

        @cache
        def rec(i, j):
            if i == m and j == n: return 0
            elif i == m: return n-j
            elif j == n: return m-i

            if word1[i] == word2[j]:
                return rec(i+1, j+1)
            
            return min(rec(i+1, j), rec(i, j+1), rec(i+1, j+1)) + 1
        
        return rec(0, 0)
