# Last updated: 12/6/2025, 5:37:20 am
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(dict)
        for x, y, w in edges:
            self.graph[x][y] = w
        
    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]][edge[1]] = edge[2]
        
    def shortestPath(self, node1: int, node2: int) -> int:
        stack = {}
        vis = {}
        stack[node1] = 0
        vis[node1] = 0
        while len(stack):
            x, m = -1, float('inf')
            for k in stack:
                if stack[k] < m:
                    x, m = k, stack[k]
            del stack[x]
            if x == node2: return m
            for y in self.graph[x]:
                w = self.graph[x][y] + m
                if y not in vis or w < vis[y]:
                    stack[y] = w
                    vis[y] = w
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)