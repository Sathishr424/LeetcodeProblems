# Last updated: 13/8/2025, 8:09:18 pm
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # 01201
        seen = {}
        arr = [str(i) for i in range(k)]
        def dfs(s, total):
            curr = s[-n:]
            if curr in seen: return None
            seen[curr] = 1

            if total == 0: return s
            for i in range(k):
                ans = dfs(s + arr[i], total - 1)
                if ans: return ans
            del seen[curr]
            return None
        
        return dfs('0' * n, k ** n - 1)