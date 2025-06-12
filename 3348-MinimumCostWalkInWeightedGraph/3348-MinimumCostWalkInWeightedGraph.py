# Last updated: 12/6/2025, 5:35:46 am
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        inf = 10**5+1
        parents = [i for i in range(n)]
        cost = [inf] * n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y, w):
            node1 = find(x)
            node2 = find(y)

            if node1 == node2:
                cost[node1] &= w
                return 1
            
            if cost[node2] < cost[node1]:
                node1, node2 = node2, node1
            
            if cost[node1] == inf:
                cost[node1] = w
            else:
                if cost[node2] == inf:
                    cost[node1] &= w
                else:
                    cost[node1] &= cost[node2] & w
            
            parents[node2] = node1
            return 0
        
        for x, y, w in edges:
            union(x, y, w)
            # union(y, x, w)
        
        ret = []
        for x, y in query:
            if find(x) != find(y): ret.append(-1) 
            else: ret.append(cost[parents[x]])
        
        return ret
