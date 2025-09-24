# Last updated: 25/9/2025, 2:40:13 am
class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        total = sum(nums)

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def isGood(mid):
            removed = 0
            def dfs(x, par):
                nonlocal removed
                s = nums[x]
                for y in graph[x]:
                    if y == par: continue
                    curr = dfs(y, x)
                    if curr < mid:
                        s += curr
                    elif curr == mid:
                        removed += 1
                    else:
                        return inf
                return s
            return dfs(0, -1) == mid, removed

        arr = []
        for i in range(n, 0, -1):
            if total % i == 0:
                can, removed = isGood(total // i)
                if can: return removed
        
        return 0