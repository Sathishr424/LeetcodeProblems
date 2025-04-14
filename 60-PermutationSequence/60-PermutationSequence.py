# Last updated: 14/4/2025, 6:24:52 pm
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        vis = {}
        for i in range(1, n+1):
            vis[i] = 1

        index = 1
        ret = []
        def rec(p):
            nonlocal index
            if len(p) == n:
                if index == k: return p
                index += 1
                return []
            
            for i in range(1, n+1):
                if vis[i]:
                    vis[i] = 0
                    p.append(i)
                    if rec(p): return p
                    p.pop()
                    vis[i] = 1

            return []
        
        return ''.join([str(i) for i in rec([])])