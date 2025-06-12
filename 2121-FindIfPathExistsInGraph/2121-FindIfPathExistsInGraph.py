# Last updated: 12/6/2025, 5:39:10 am
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(dict)

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            node1 = find(x)
            node2 = find(y)

            if node1 == node2: return True

            if rank[node2] > rank[node1]:
                node1, node2 = node2, node1
            
            rank[node1] += rank[node2]
            parent[node2] = node1
            
            return False
        
        for x, y in edges:
            union(x, y)
        
        return union(source, destination)