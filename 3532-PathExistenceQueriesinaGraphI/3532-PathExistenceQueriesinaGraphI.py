# Last updated: 27/4/2025, 5:25:03 pm
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parents = [i for i in range(n)]
        sizes = [1] * n

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            node1 = find(x)
            node2 = find(y)

            if node1 == node2: return True
            if sizes[node2] > sizes[node1]:
                node1, node2 = node2, node1
            
            sizes[node1] += sizes[node2]
            parents[node2] = node1
            return False
        
        for i in range(1, n):
            if nums[i] - nums[i-1] <= maxDiff:
                union(i-1, i)
        ret = []
        for x, y in queries:
            ret.append(find(x) == find(y))
        
        return ret