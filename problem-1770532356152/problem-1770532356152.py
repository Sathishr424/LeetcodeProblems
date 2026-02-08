# Last updated: 2/8/2026, 12:02:36 PM
1from math import floor, log2
2
3class sparseTableMin:
4    def __init__(self, nums):
5        self.nums = nums
6        n = len(nums)
7        self.n = n
8        k_log = floor(log2(n)) + 1
9                
10        self.max_logs = [[0] * n for _ in range(k_log)]
11
12        for i in range(n):
13            self.max_logs[0][i] = nums[i]
14
15        for power in range(1, k_log):
16            m = 1 << power
17            prev_m = m >> 1
18
19            for i in range(n-m+1):
20                self.max_logs[power][i] = min(self.max_logs[power - 1][i], self.max_logs[power - 1][i + prev_m])
21    
22    def query(self, l, r):
23        dis = r - l + 1
24        power = floor(log2(dis))
25        return min(self.max_logs[power][l], self.max_logs[power][r - (1 << power) + 1])
26        
27class sparseTableMax:
28    def __init__(self, nums):
29        self.nums = nums
30        n = len(nums)
31        self.n = n
32        k_log = floor(log2(n)) + 1
33                
34        self.max_logs = [[0] * n for _ in range(k_log)]
35
36        for i in range(n):
37            self.max_logs[0][i] = nums[i]
38
39        for power in range(1, k_log):
40            m = 1 << power
41            prev_m = m >> 1
42
43            for i in range(n-m+1):
44                self.max_logs[power][i] = max(self.max_logs[power - 1][i], self.max_logs[power - 1][i + prev_m])
45    
46    def query(self, l, r):
47        dis = r - l + 1
48        power = floor(log2(dis))
49        return max(self.max_logs[power][l], self.max_logs[power][r - (1 << power) + 1])
50        
51class sparseTableMax:
52    def __init__(self, nums):
53        self.nums = nums
54        n = len(nums)
55        self.n = n
56        k_log = floor(log2(n)) + 1
57                
58        self.max_logs = [[0] * n for _ in range(k_log)]
59
60        for i in range(n):
61            self.max_logs[0][i] = nums[i]
62
63        for power in range(1, k_log):
64            m = 1 << power
65            prev_m = m >> 1
66
67            for i in range(n-m+1):
68                self.max_logs[power][i] = max(self.max_logs[power - 1][i], self.max_logs[power - 1][i + prev_m])
69    
70    def query(self, l, r):
71        dis = r - l + 1
72        power = floor(log2(dis))
73        return max(self.max_logs[power][l], self.max_logs[power][r - (1 << power) + 1])
74        
75class Solution:
76    def countSubarrays(self, nums: List[int], k: int) -> int:
77        n = len(nums)
78
79        maxTable = sparseTableMax(nums)
80        minTable = sparseTableMin(nums)
81
82        left = 0
83        ans = 0
84
85        for i in range(n):
86            while (i - left + 1) * (maxTable.query(left, i) - minTable.query(left, i)) > k:
87                left += 1
88
89            ans += i - left + 1
90
91        return ans
92        