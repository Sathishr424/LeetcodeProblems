# Last updated: 7/11/2026, 6:06:55 AM
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
14        # print(arr)
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
28            # print(p)
29            # [print(row) for row in logs]
30
31        # print(logs[0])
32        ret = []
33        for l, r in queries:
34            left = indexes[l]
35            right = indexes[r]
36
37            if left > right:
38                left, right = right, left
39
40            val = 0
41            for p in range(self.k - 1, -1, -1):
42                if logs[p][left] != -1 and logs[p][left] <= right:
43                    val += 1 << p
44                    left = logs[p][left]
45
46            if left < right and logs[0][left] < right: val = -1
47            elif left != right: val += 1
48            ret.append(val)
49            # print((l, r), (left, right), val)
50
51        return ret