# Last updated: 26/7/2025, 2:36:16 am
class Solution:
    def calculateMinimumHP(self, dung: List[List[int]]) -> int:
        m = len(dung)
        n = len(dung[0])

        @cache
        def dfs(i, j, health):
            health += dung[i][j]
            if health <= 0: return False
            if i == m-1 and j == n-1:
                return True
            
            if i + 1 < m:
                if dfs(i + 1, j, health): return True
            if j + 1 < n:
                if dfs(i, j + 1, health): return True
            return False
        
        l = 1
        r = m * n * 1000

        while l < r:
            mid = (l + r) // 2

            if dfs(0, 0, mid):
                r = mid
            else:
                l = mid + 1
        
        return l