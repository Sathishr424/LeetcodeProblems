# Last updated: 26/7/2025, 6:06:41 am
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = defaultdict(list)

        for x, y, t in edges:
            graph[x].append((y, t))
            graph[y].append((x, t))
        
        stack = deque([(0, maxTime, 0, {0: 1})])
        ret = 0

        while stack:
            node, remTime, parent, vis = stack.popleft()
            if node == 0:
                ans = 0
                for x in vis:
                    ans += values[x]
                ret = max(ret, ans)

            for child, t in graph[node]:
                if remTime - t < 0: continue
                new_vis = dict(vis)
                new_vis[child] = 1
                stack.append((child, remTime - t, node, new_vis))
        
        return ret