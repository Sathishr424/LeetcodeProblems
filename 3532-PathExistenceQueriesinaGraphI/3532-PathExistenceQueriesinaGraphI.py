# Last updated: 7/9/2026, 3:59:12 PM
1class Union:
2    def __init__(self, n):
3        self.parents = [i for i in range(n)]
4        self.sizes = [1] * n
5
6    def find(self, x):
7        if x != self.parents[x]:
8            self.parents[x] = self.find(self.parents[x])
9
10        return self.parents[x]
11
12    def union(self, x, y):
13        x = self.find(x)
14        y = self.find(y)
15
16        if x == y: return True
17
18        if self.sizes[y] > self.sizes[x]:
19            x, y = y, x
20
21        self.sizes[x] += self.sizes[y]
22        self.parents[y] = x
23        
24        return False
25
26class Solution:
27    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
28        un = Union(n)
29
30        left = 0
31        for i in range(n):
32            while nums[i] - nums[left] > maxDiff:
33                left += 1
34            un.union(left, i)
35
36        ret = []
37        for l, r in queries:
38            ret.append(un.find(l) == un.find(r))
39        return ret