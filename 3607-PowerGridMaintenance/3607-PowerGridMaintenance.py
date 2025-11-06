# Last updated: 6/11/2025, 2:01:34 pm
class Union:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n

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
        
        return False

class Solution:
    def processQueries(self, n: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        un = Union(n)

        for u, v in connections:
            un.union(u-1, v-1)
        
        parents = defaultdict(lambda: SortedList())

        for i in range(n):
            parents[un.find(i)].add(i)
        
        ret = []
        online = [1] * n
        for t, node in queries:
            node -= 1
            if t == 1:
                if online[node]:
                    ret.append(node + 1)
                else:
                    par = un.find(node)
                    ret.append(parents[par][0] + 1 if len(parents[par]) else -1)
            else:
                par = un.find(node)
                online[node] = 0
                parents[par].discard(node)
        
        return ret
