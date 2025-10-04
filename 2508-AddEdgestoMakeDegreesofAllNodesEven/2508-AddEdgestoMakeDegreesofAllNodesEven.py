# Last updated: 4/10/2025, 10:37:17 pm
class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        out_degree = [0] * n
        graph = defaultdict(dict)
        out = 0

        for x, y in edges:
            x -= 1
            y -= 1
            out_degree[y] += 1
            out_degree[x] += 1
            graph[x][y] = 1
            graph[y][x] = 1
        
        for i in range(n):
            if out_degree[i] % 2:
                out += 1
        
        def connect(x, y, degree):
            if x not in graph[y]: 
                return 1
            for i in range(n):
                if degree[i] % 2 == 0 and i not in graph[x] and i not in graph[y]:
                    return 2
            return 5
        
        if out == 0: return True
        if out % 2 or out > 4: return False
        if out == 2:
            nodes = []
            for i in range(n):
                if out_degree[i] % 2:
                    nodes.append(i)
            x, y = nodes
            return connect(x, y, out_degree) <= 2
        else:
            nodes = []
            for i in range(n):
                if out_degree[i] % 2:
                    nodes.append(i)
            for i in range(4):
                for j in range(i+1, 4):
                    k, l = [m for m in range(4) if m != i and m != j]
                    if connect(nodes[i], nodes[j], out_degree) + connect(nodes[k], nodes[l], out_degree) <= 2:
                        return True
            return False