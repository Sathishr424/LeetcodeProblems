# Last updated: 27/4/2025, 5:28:42 pm
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parents = [i for i in range(n)]

        def find(x):
            return parents[x]
        
        def union(x, y):
            parents[find(y)] = find(x)
        
        for i in range(1, n):
            if nums[i] - nums[i-1] <= maxDiff:
                union(i-1, i)
        
        ret = []

        for x, y in queries:
            ret.append(find(x) == find(y))
        
        return ret