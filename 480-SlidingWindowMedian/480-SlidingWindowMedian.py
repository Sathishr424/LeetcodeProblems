# Last updated: 1/12/2025, 2:26:33 am
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
48        self.remove_deleted()
49        heapq.heappush(self.right, -heapq.heappop(self.left))
50        
51        self.remove_deleted()
52        
53        self.adjust_left_right()
54        
55        self.remove_deleted()
56
57        self.adjust_left_right()
58    
59    def getMedian(self):
60        n = self.getSize()
61        if n % 2:
62            return -self.left[0]
63        else:
64            return (-1 * self.left[0] + self.right[0]) / 2
65
66class Solution:
67    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
68        n = len(nums)
69        ret = []
70
71        dm = DynamicMedian()
72
73        for i in range(k):
74            dm.add(nums[i])
75
76        ret.append(dm.getMedian())
77
78        for i in range(k, n):
79            dm.remove(nums[i - k])
80            dm.add(nums[i])
81
82            ret.append(dm.getMedian())
83
84        return ret