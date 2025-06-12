# Last updated: 12/6/2025, 5:47:40 am
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n)]

        def find(x):
            if parents[x] != x:
                return find(parents[x])
            return parents[x]
        
        def union(x, y):
            node1 = find(x)
            node2 = find(y)

            if node1 == node2: return True

            parents[node2] = node1
            return False

        for x, y in edges:
            if union(x-1, y-1): return [x, y]        
