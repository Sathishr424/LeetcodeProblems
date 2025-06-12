# Last updated: 12/6/2025, 5:50:40 am
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(dict)

        for x, y in edges:
            graph[x][y] = 1
            graph[y][x] = 1
        
        leaves = deque([])
        edge_count = {}
        for x in range(n):
            if len(graph[x]) <= 1: leaves.append(x)
            edge_count[x] = len(graph[x])
        
        while n > 2:
            for i in range(len(leaves)):
                x = leaves.popleft()
                n -= 1
                for y in graph[x]:
                    edge_count[y] -= 1
                    if edge_count[y] == 1:
                        leaves.append(y)

        return list(leaves)