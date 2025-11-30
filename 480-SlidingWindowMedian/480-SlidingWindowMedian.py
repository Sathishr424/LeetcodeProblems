# Last updated: 1/12/2025, 2:48:30 am
1class DynamicMedian:
2    def __init__(self):
3        self.left = []
4        self.right = []
5        self.left_delete = defaultdict(int)
6        self.right_delete = defaultdict(int)
7        self.left_delete_cnt = 0
8        self.right_delete_cnt = 0
9        self.left_sum = 0
10        self.right_sum = 0
11    
12    def getLeftSize(self):
13        return len(self.left) - self.left_delete_cnt
14    
15    def getRightSize(self):
16        return len(self.right) - self.right_delete_cnt
17
18    def getSize(self):
19        return len(self.left) + len(self.right) - (self.left_delete_cnt + self.right_delete_cnt)
20    
21    def remove_deleted(self):
22        while self.left and self.left_delete[-self.left[0]]:
23            num = -heapq.heappop(self.left)
24            self.left_delete[num] -= 1
25            self.left_delete_cnt -= 1
26
27        while self.right and self.right_delete[self.right[0]]:
28            num = heapq.heappop(self.right)
29            self.right_delete[num] -= 1
30            self.right_delete_cnt -= 1
31
32    def adjust_left_right(self):
33        self.left_cnt = self.getLeftSize()
34        self.right_cnt = self.getRightSize()
35        
36        n = self.getSize()
37        ceil_half = ceil(n / 2)
38        half = n // 2
39
40        if self.left_cnt > ceil_half:
41            self.left_sum -= -self.left[0]
42            self.right_sum += -self.left[0]
43            heapq.heappush(self.right, -heapq.heappop(self.left))
44        
45        if self.right_cnt > half:
46            self.left_sum += self.right[0]
47            self.right_sum -= self.right[0]
48            heapq.heappush(self.left, -heapq.heappop(self.right))
49    
50    def remove(self, num):
51        if not self.right or num < self.right[0]:
52            self.left_delete[num] += 1
53            self.left_delete_cnt += 1
54            self.left_sum -= num
55        else:
56            self.right_delete[num] += 1
57            self.right_delete_cnt += 1
58            self.right_sum -= num
59
60        self.adjust_left_right()
61        self.remove_deleted()
62
63    def add(self, num):
64        self.left_sum += num
65        heapq.heappush(self.left, -num)
66        self.left_sum -= -self.left[0]
67        self.right_sum += -self.left[0]
68        heapq.heappush(self.right, -heapq.heappop(self.left))
69        
70        self.adjust_left_right()
71        
72        self.remove_deleted()
73    
74    def getMedian(self):
75        n = self.getSize()
76        if n % 2:
77            return -self.left[0]
78        else:
79            return (-1 * self.left[0] + self.right[0]) / 2
80
81class Solution:
82    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
83        n = len(nums)
84        ret = []
85
86        dm = DynamicMedian()
87
88        for i in range(k):
89            dm.add(nums[i])
90
91        ret.append(dm.getMedian())
92
93        for i in range(k, n):
94            dm.remove(nums[i - k])
95            dm.add(nums[i])
96
97            ret.append(dm.getMedian())
98
99        return ret