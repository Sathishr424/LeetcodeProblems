# Last updated: 3/12/2025, 3:33:36 pm
1class PSegmentTree:
2    def __init__(self, n, nums, compressed):
3        self.n = n
4        self.roots = []
5        self.lefts = []
6        self.rights = []
7        self.sums = []
8        self.cnts = []
9        self.node_index = 0
10        self.roots.append(self.build(0, n-1))
11        for i, num in enumerate(nums):
12            self.roots.append(self.update(self.roots[-1], 0, self.n-1, compressed[(num, i)], num))
13
14    def getNewNode(self, l=-1, r=-1, cnt=0, sum=0):
15        if l != -1 and r != -1:
16            cnt = self.cnts[l] + self.cnts[r]
17            sum = self.sums[l] + self.sums[r]
18        self.cnts.append(cnt)
19        self.sums.append(sum)
20        self.lefts.append(l)
21        self.rights.append(r)
22        self.node_index += 1
23        return self.node_index - 1
24    
25    def build(self, l, r):
26        if l == r: return self.getNewNode()
27        mid = (l + r) // 2
28
29        return self.getNewNode(self.build(l, mid), self.build(mid + 1, r))
30    
31    def nodeAt(self, index):
32        return self.nodes[index]
33
34    def update(self, node, l, r, pos, sum):
35        if l == r:
36            return self.getNewNode(cnt=self.cnts[node] + 1, sum=self.sums[node] + sum)
37        
38        mid = (l + r) // 2
39
40        if pos <= mid:
41            return self.getNewNode(self.update(self.lefts[node], l, mid, pos, sum), self.rights[node])
42        return self.getNewNode(self.lefts[node], self.update(self.rights[node], mid + 1, r, pos, sum))
43    
44    def _getKthSmallest(self, left, right, l, r, k):
45        if l == r:
46            return l
47        
48        mid = (l + r) // 2
49        left_count = self.cnts[self.lefts[right]]- self.cnts[self.lefts[left]]
50        if left_count >= k:
51            return self._getKthSmallest(self.lefts[left], self.lefts[right], l, mid, k)
52        return self._getKthSmallest(self.rights[left], self.rights[right], mid + 1, r, k - left_count)
53    
54    def _getFirstKSum(self, left, right, l, r, k):
55        if l == r:
56            return self.sums[right] - self.sums[left]
57        
58        mid = (l + r) // 2
59        left_count = self.cnts[self.lefts[right]]- self.cnts[self.lefts[left]]
60        if left_count >= k:
61            return self._getFirstKSum(self.lefts[left], self.lefts[right], l, mid, k)
62        return (self.sums[self.lefts[right]] - self.sums[self.lefts[left]]) + self._getFirstKSum(self.rights[left], self.rights[right], mid + 1, r, k - left_count)
63
64    def getKthSmallest(self, l, r, k):
65        return self._getKthSmallest(self.roots[l], self.roots[r+1], 0, self.n-1, k)
66    
67    def getFirstKSum(self, l, r, k):
68        return self._getFirstKSum(self.roots[l], self.roots[r+1], 0, self.n-1, k)
69
70class Solution:
71    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
72        n = len(nums)
73        divided = []
74        prefix = [0]
75        new_nums = []
76        for i, num in enumerate(nums):
77            divided.append(num // k)
78            prefix.append(prefix[-1] + divided[-1])
79            new_nums.append((divided[-1], i))
80        compressed = {}
81        uncompressed = [0] * n
82        new_nums.sort()
83        index = 0
84        for num, i in new_nums:
85            compressed[(num, i)] = index
86            uncompressed[index] = num
87            index += 1
88        
89        same_group = [0] * n
90        i = 0
91        group = 0
92        while i < n:
93            rem = nums[i] % k
94            while i < n and nums[i] % k == rem:
95                same_group[i] = group
96                i += 1
97            group += 1
98
99        segTree = PSegmentTree(index, divided, compressed)
100        ret = []
101        for l, r in queries:
102            if same_group[l] != same_group[r]:
103                ret.append(-1)
104                continue
105            
106            window = r - l + 1
107            half = window // 2
108            if window % 2:
109                med = segTree.getKthSmallest(l, r, half + 1)
110                median = uncompressed[med]
111                leftSum = segTree.getFirstKSum(l, r, half + 1)
112                remSum = (prefix[r + 1] - prefix[l]) - leftSum
113                ret.append((median * (half + 1) - leftSum) + (remSum - median * half))
114            else:
115                median_l = uncompressed[segTree.getKthSmallest(l, r, half)]
116                median_r = uncompressed[segTree.getKthSmallest(l, r, half + 1)]
117                median = (median_l + median_r) // 2
118                leftSum = segTree.getFirstKSum(l, r, half)
119                remSum = (prefix[r + 1] - prefix[l]) - leftSum
120                ret.append((median * half - leftSum) + (remSum - median * half))
121        
122        return ret