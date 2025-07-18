# Last updated: 12/6/2025, 5:35:12 am
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        m = len(edges1) + 1
        n = len(edges2) + 1

        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for x, y in edges1:
            graph1[x].append(y)
            graph1[y].append(x)
        for x, y in edges2:
            graph2[x].append(y)
            graph2[y].append(x)
        
        def bfs(graph, odds):
            stack = [(0, -1)]
            depth = 0

            while stack:
                new_stack = []
                for x, par in stack:
                    odds[x] = depth % 2
                    for y in graph[x]:
                        if y == par: continue
                        new_stack.append((y, x))
                depth += 1
                stack = new_stack
        
        odds_index = [0] * m
        bfs(graph1, odds_index)
        odds1 = sum(odds_index)
        evens1 = m - odds1

        odds2 = [0] * n
        bfs(graph2, odds2)
        odds2 = sum(odds2)
        evens2 = n - odds2

        maxi = max(odds2, evens2)
        ret = [evens1 + maxi]
        for i in range(1, m):
            if odds_index[i] == 1:
                ret.append(odds1 + maxi)
            else:
                ret.append(evens1 + maxi)
        
        return ret