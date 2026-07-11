# Last updated: 7/11/2026, 6:16:19 AM
1class Solution:
2    k = 32
3    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
4        self.k = n.bit_length()
5        new_nums = []
6        indexes = [0] * n
7        for i in range(n):
8            new_nums.append((nums[i], i))
9        new_nums.sort()
10
11        arr = []
12        for i in range(n):
13            indexes[new_nums[i][1]] = i
14            arr.append(new_nums[i][0])
15
16        logs = [[-1] * n for _ in range(self.k)]
17        for i in range(n):
18            index = bisect_right(arr, arr[i] + maxDiff) - 1
19            if index == i:
20                index = -1
21            logs[0][i] = index
22
23        for p in range(1, self.k):
24            for i in range(n):
25                if logs[p-1][i] != -1:
26                    logs[p][i] = logs[p - 1][logs[p - 1][i]]
27
28        ret = []
29        for l, r in queries:
30            left = indexes[l]
31            right = indexes[r]
32
33            if left > right:
34                left, right = right, left
35
36            val = 0
37            for p in range(self.k - 1, -1, -1):
38                if logs[p][left] != -1 and logs[p][left] <= right:
39                    val += 1 << p
40                    left = logs[p][left]
41
42            if left < right and logs[0][left] < right: val = -1
43            elif left != right: val += 1
44            ret.append(val)
45
46        return ret