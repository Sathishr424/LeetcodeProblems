# Last updated: 12/8/2025, 3:36:54 pm
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
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])

        un = Union(n)
        un.union(0, firstPerson)

        linked = []
        last_added = defaultdict(list)
        prev = -1

        def dfs(x, vis):
            if x in vis: return
            vis[x] = 1
            for y in last_added[x]:
                un.union(x, y)
                dfs(y, vis)
        
        for x, y, t in meetings:
            if t != prev:
                vis = {}
                for node in linked:
                    dfs(node, vis)
                linked = []
                last_added = defaultdict(list)
                    
            if un.find(x) == 0 or un.find(y) == 0:
                un.union(x, y)
                linked.append(x)
                linked.append(y)
            else:
                last_added[x].append(y)
                last_added[y].append(x)

            prev = t

        vis = {}
        for node in linked:
            dfs(node, vis)
        
        ret = []

        for i in range(n):
            if un.find(i) == 0:
                ret.append(i)

        return ret
        