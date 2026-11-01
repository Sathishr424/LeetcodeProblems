# Last updated: 11/1/2026, 10:19:20 PM
1class Solution:
2    def minOperationsBubbleSort(self, nums: list[int], locked: list[int], k: int) -> int:
3        n = len(nums)
4
5        op = 0
6        ans = 0
7        def bubbleSort(nums):
8            nonlocal op, ans
9            is_sorted = True
10            for i in range(n-1):
11                if nums[i] > nums[i + 1]:
12                    if locked[i] == 1:
13                        if op == k: return False, nums
14                        op += 1
15                        locked[i] = 0
16                    if locked[i + 1] == 1:
17                        if op == k: return False, nums
18                        op += 1
19                        locked[i + 1] = 0
20
21                    nums[i + 1], nums[i] = nums[i], nums[i + 1]
22                    ans += 1
23                    is_sorted = False
24            if is_sorted: return True, nums
25            return bubbleSort(nums)
26
27        is_sorted, nums = bubbleSort(nums)
28        if not is_sorted: return -1
29        return op + ans
30
31    def minOperations(self, nums: list[int], locked: list[int], can: int) -> int:
32        n = len(nums)
33        op = 0
34        ans = 0
35        def mergeSort(array: list):
36            nonlocal op, ans
37            if len(array) <= 1: return True
38            m = len(array)
39            half = m // 2
40            left = array[:half]
41            right = array[half:]
42            if not mergeSort(left): return False
43            if not mergeSort(right): return False
44
45            l = 0
46            r = 0
47            k = 0
48
49            cnt = 0
50            while l < len(left) and r < len(right):
51                if left[l][0] <= right[r][0]:
52                    if cnt > 0 and left[l][1] == 1:
53                        if op == can: return False
54                        left[l] = (left[l][0], 0)
55                        op += 1
56                    array[k] = left[l]
57                    l += 1
58                    ans += cnt
59                else:
60                    if left[l][1] == 1:
61                        if op == can: return False
62                        left[l] = (left[l][0], 0)
63                        op += 1
64                    if right[r][1] == 1:
65                        if op == can: return False
66                        right[r] = (right[r][0], 0)
67                        op += 1
68                    array[k] = right[r]
69                    r += 1
70                    cnt += 1
71                k += 1
72
73            while l < len(left):
74                if left[l][1] == 1:
75                    if op == can: return False
76                    left[l] = (left[l][0], 0)
77                    op += 1
78                array[k] = left[l]
79                l += 1
80                k += 1
81                ans += cnt
82
83            while r < len(right):
84                array[k] = right[r]
85                r += 1
86                k += 1
87
88            return True
89
90        if not mergeSort([(nums[i], locked[i]) for i in range(n)]): return -1
91        return op + ans