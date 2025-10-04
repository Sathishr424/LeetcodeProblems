# Last updated: 4/10/2025, 10:39:59 pm
class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        out_degree = [0] * n
        graph = defaultdict(dict)
        out = []

        for x, y in edges:
            x -= 1
            y -= 1
            out_degree[y] += 1
            out_degree[x] += 1
            graph[x][y] = 1
            graph[y][x] = 1
        
        for i in range(n):
            if out_degree[i] % 2:
                out.append(i)
        
        def connect(x, y):
            if x not in graph[y]: 
                return 1
            for i in range(n):
                if out_degree[i] % 2 == 0 and i not in graph[x] and i not in graph[y]:
                    return 2
            return 5
        
        if len(out) == 0: return True
        if len(out) % 2 or len(out) > 4: return False
        if len(out) == 2:
            return connect(*out) <= 2
        else:
            for i in range(4):
                for j in range(i+1, 4):
                    k, l = [m for m in range(4) if m != i and m != j]
                    if connect(out[i], out[j]) + connect(out[k], out[l]) <= 2:
                        return True
            return False