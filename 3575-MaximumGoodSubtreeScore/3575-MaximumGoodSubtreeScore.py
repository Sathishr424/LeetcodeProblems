# Last updated: 7/6/2025, 9:38:49 pm
class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        n = len(vals)
        mod = 10**9 + 7

        valMasks = [0] * n
        canAdd = [0] * n

        for i, val in enumerate(vals):
            mask = 0
            while val:
                rem = val % 10
                if mask & (1 << rem) != 0:
                    break
                mask |= (1 << rem)
                val //= 10

            if val == 0:
                valMasks[i] = mask
                canAdd[i] = 1
            else:
                canAdd[i] = 0
            
        graph = defaultdict(list)

        for i in range(1, n):
            graph[par[i]].append(i)

        childs = [[] for _ in range(n)]

        def dfs(x):
            childs[x].append(x)
            for y in graph[x]:
                dfs(y)
                childs[x] += childs[y]
        
        dfs(0)

        memo = {}
        def rec(child, index, mask):
            if mask in memo: return memo[mask]
            if index == len(child): return 0
            ans = 0
            if canAdd[child[index]] and mask & valMasks[child[index]] == 0:
                ans = max(ans, rec(child, index+1, mask | valMasks[child[index]]) + vals[child[index]])
            ans = max(ans, rec(child, index+1, mask))
            memo[mask] = ans
            return ans
        
        ret = 0
        for i in range(n):
            memo = {}
            score = rec(childs[i], 0, 0)
            ret = (ret + score) % mod

        return ret
            
                            