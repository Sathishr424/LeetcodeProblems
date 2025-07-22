# Last updated: 23/7/2025, 3:00:49 am
class Union:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
        self.cnt = 1
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y: return True
        
        if self.sizes[y] > self.sizes[x]:
            x, y = y, x
        self.sizes[x] += self.sizes[y]
        self.parents[y] = x
        self.cnt += 1
        return False

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        def unionConnect(index):
            un = Union(n)

            for i in range(n):
                if i == index: continue
                un.union(edges[i][0] - 1, edges[i][1] - 1)
        
            if un.cnt == n:
                return index
            return -1
        
        graph = defaultdict(dict)
        reverse = defaultdict(list)

        for i in range(n-1, -1, -1):
            graph[edges[i][0]][edges[i][1]] = i
            reverse[edges[i][1]].append(i)
        
        for i in range(1, n+1):
            if len(reverse[i]) > 1:
                for index in reverse[i]:
                    if unionConnect(index) == index: return edges[index] 
        
        un = Union(n)
        ans = 0
        for i in range(n):
            if un.union(edges[i][0] - 1, edges[i][1] - 1):
                ans = i
        
        return edges[ans]
            