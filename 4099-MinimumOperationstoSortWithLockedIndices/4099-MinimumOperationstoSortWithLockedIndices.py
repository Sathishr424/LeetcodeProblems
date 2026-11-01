# Last updated: 11/1/2026, 10:15:11 PM
1class Solution:
2    def minOperations(self, nums: list[int], locked: list[int], can: int) -> int:
3        n = len(nums)
4        op = 0
5        ans = 0
6        def mergeSort(array: list):
7            nonlocal op, ans
8            if len(array) <= 1: return True
9            m = len(array)
10            half = m // 2
11            left = array[:half]
12            right = array[half:]
13            if not mergeSort(left): return False
14            if not mergeSort(right): return False
15
16            l = 0
17            r = 0
18            k = 0
19
20            cnt = 0
21            while l < len(left) and r < len(right):
22                if left[l][0] <= right[r][0]:
23                    if cnt > 0 and left[l][1] == 1:
24                        if op == can: return False
25                        left[l] = (left[l][0], 0)
26                        op += 1
27                    array[k] = left[l]
28                    l += 1
29                    ans += cnt
30                else:
31                    if left[l][1] == 1:
32                        if op == can: return False
33                        left[l] = (left[l][0], 0)
34                        op += 1
35                    if right[r][1] == 1:
36                        if op == can: return False
37                        right[r] = (right[r][0], 0)
38                        op += 1
39                    array[k] = right[r]
40                    r += 1
41                    cnt += 1
42                k += 1
43
44            while l < len(left):
45                if left[l][1] == 1:
46                    if op == can: return False
47                    left[l] = (left[l][0], 0)
48                    op += 1
49                array[k] = left[l]
50                l += 1
51                k += 1
52                ans += cnt
53
54            while r < len(right):
55                array[k] = right[r]
56                r += 1
57                k += 1
58
59            return True
60
61        if not mergeSort([(nums[i], locked[i]) for i in range(n)]): return -1
62        return op + ans