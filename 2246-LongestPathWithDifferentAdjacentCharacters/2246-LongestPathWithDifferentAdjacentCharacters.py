# Last updated: 9/9/2025, 9:52:56 pm
class Solution:
    def longestPath(self, parent: List[int], relation: str) -> int:
        n = len(parent)
        graph = defaultdict(list)
        edges = []

        for i in range(1, n):
            par = parent[i]
            graph[par].append(i)
            graph[i].append(par)
        
        max_ans = 1
        
        def dfs(x, par, prev, curr):
            nonlocal max_ans
            ans = curr
            f1 = 0
            f2 = 0
            for y in graph[x]:
                if y == par: continue
                new_curr = dfs(y, x, relation[y], 1)
                if relation[y] != prev:
                    if new_curr > f1:
                        f2 = f1
                        f1 = new_curr
                    elif new_curr > f2:
                        f2 = new_curr
                    ans = max(ans, new_curr + curr)
            
            max_ans = max(max_ans, f1 + f2 + 1)

            return ans
        
        dfs(0, -1, relation[0], 1)
        return max_ans