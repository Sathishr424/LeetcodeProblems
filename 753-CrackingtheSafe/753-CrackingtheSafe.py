# Last updated: 13/8/2025, 8:07:47 pm
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # 01201
        seen = {}
        def dfs(s, curr, total):
            if curr in seen: return None

            seen[curr] = 1
            if total == 0: return s
            new_curr = curr[1:]
            for i in range(k):
                ans = dfs(s + str(i), new_curr + str(i), total - 1)
                if ans: return ans
            del seen[curr]
            return None
        
        return dfs('0' * n, '0' * n, k ** n - 1)