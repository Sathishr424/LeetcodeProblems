# Last updated: 10/17/2026, 9:49:13 PM
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
27    def minSwaps(self, nums: List[int]) -> int:
28        n = len(nums)
29
30        sorted_arr = []
31        for i, num in enumerate(nums):
32            s = 0
33            while num:
34                s += num % 10
35                num //= 10
36            sorted_arr.append((s, nums[i], i))
37
38        sorted_arr.sort()
39        un = Union(n)
40        ans = 0
41        for i in range(n):
42            if not un.union(i, sorted_arr[i][-1]):
43                ans += 1
44
45        return ans
46