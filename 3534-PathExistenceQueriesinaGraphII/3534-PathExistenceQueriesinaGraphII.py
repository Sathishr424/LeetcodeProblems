# Last updated: 7/11/2026, 6:10:48 AM
1class Solution:
2    k = 32
3    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
4        new_nums = []
5        indexes = [0] * n
6        for i in range(n):
7            new_nums.append((nums[i], i))
8        new_nums.sort()
9
10        arr = []
11        for i in range(n):
12            indexes[new_nums[i][1]] = i
13            arr.append(new_nums[i][0])
14
15        logs = [[-1] * n for _ in range(self.k)]
16        for i in range(n):
17            index = bisect_right(arr, arr[i] + maxDiff) - 1
18            if index == i:
19                index = -1
20            logs[0][i] = index
21
22        for p in range(1, self.k):
23            for i in range(n):
24                if logs[p-1][i] != -1:
25                    logs[p][i] = logs[p - 1][logs[p - 1][i]]
26
27        ret = []
28        for l, r in queries:
29            left = indexes[l]
30            right = indexes[r]
31
32            if left > right:
33                left, right = right, left
34
35            val = 0
36            for p in range(self.k - 1, -1, -1):
37                if logs[p][left] != -1 and logs[p][left] <= right:
38                    val += 1 << p
39                    left = logs[p][left]
40
41            if left < right and logs[0][left] < right: val = -1
42            elif left != right: val += 1
43            ret.append(val)
44
45        return ret