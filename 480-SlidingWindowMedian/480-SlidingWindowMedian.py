# Last updated: 1/12/2025, 2:27:02 am
1class DynamicMedian:
2    def __init__(self):
3        self.left = []
4        self.right = []
5        self.left_delete = defaultdict(int)
6        self.right_delete = defaultdict(int)
7        self.left_delete_cnt = 0
8        self.right_delete_cnt = 0
9    
10    def getSize(self):
11        return len(self.left) + len(self.right) - (self.left_delete_cnt + self.right_delete_cnt)
12    
13    def remove_deleted(self):
14        while self.left and self.left_delete[-self.left[0]]:
15            num = -heapq.heappop(self.left)
16            self.left_delete[num] -= 1
17            self.left_delete_cnt -= 1
18
19        while self.right and self.right_delete[self.right[0]]:
20            num = heapq.heappop(self.right)
21            self.right_delete[num] -= 1
22            self.right_delete_cnt -= 1
23
24    def adjust_left_right(self):
25        self.left_cnt = len(self.left) - self.left_delete_cnt
26        self.right_cnt = len(self.right) - self.right_delete_cnt
27        
28        n = self.getSize()
29        ceil_half = ceil(n / 2)
30        half = n // 2
31
32        if self.left_cnt > ceil_half:
33            heapq.heappush(self.right, -heapq.heappop(self.left))
34        
35        if self.right_cnt > half:
36            heapq.heappush(self.left, -heapq.heappop(self.right))
37    
38    def remove(self, num):
39        if not self.right or num < self.right[0]:
40            self.left_delete[num] += 1
41            self.left_delete_cnt += 1
42        else:
43            self.right_delete[num] += 1
44            self.right_delete_cnt += 1
45
46    def add(self, num):
47        heapq.heappush(self.left, -num)
48        heapq.heappush(self.right, -heapq.heappop(self.left))
49        
50        self.remove_deleted()
51        
52        self.adjust_left_right()
53        
54        self.remove_deleted()
55    
56    def getMedian(self):
57        n = self.getSize()
58        if n % 2:
59            return -self.left[0]
60        else:
61            return (-1 * self.left[0] + self.right[0]) / 2
62
63class Solution:
64    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
65        n = len(nums)
66        ret = []
67
68        dm = DynamicMedian()
69
70        for i in range(k):
71            dm.add(nums[i])
72
73        ret.append(dm.getMedian())
74
75        for i in range(k, n):
76            dm.remove(nums[i - k])
77            dm.add(nums[i])
78
79            ret.append(dm.getMedian())
80
81        return ret