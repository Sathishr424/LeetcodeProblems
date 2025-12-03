# Last updated: 3/12/2025, 3:40:49 pm
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
31    def update(self, node, l, r, pos, sum):
32        if l == r:
33            return self.getNewNode(cnt=self.cnts[node] + 1, sum=self.sums[node] + sum)
34        
35        mid = (l + r) // 2
36
37        if pos <= mid:
38            return self.getNewNode(self.update(self.lefts[node], l, mid, pos, sum), self.rights[node])
39        return self.getNewNode(self.lefts[node], self.update(self.rights[node], mid + 1, r, pos, sum))
40    
41    def _getKthSmallest(self, left, right, l, r, k):
42        if l == r:
43            return l
44        
45        mid = (l + r) // 2
46        left_count = self.cnts[self.lefts[right]]- self.cnts[self.lefts[left]]
47        if left_count >= k:
48            return self._getKthSmallest(self.lefts[left], self.lefts[right], l, mid, k)
49        return self._getKthSmallest(self.rights[left], self.rights[right], mid + 1, r, k - left_count)
50    
51    def _getFirstKSum(self, left, right, l, r, k):
52        if l == r:
53            return self.sums[right] - self.sums[left]
54        
55        mid = (l + r) // 2
56        left_count = self.cnts[self.lefts[right]]- self.cnts[self.lefts[left]]
57        if left_count >= k:
58            return self._getFirstKSum(self.lefts[left], self.lefts[right], l, mid, k)
59        return (self.sums[self.lefts[right]] - self.sums[self.lefts[left]]) + self._getFirstKSum(self.rights[left], self.rights[right], mid + 1, r, k - left_count)
60
61    def getKthSmallest(self, l, r, k):
62        return self._getKthSmallest(self.roots[l], self.roots[r+1], 0, self.n-1, k)
63    
64    def getFirstKSum(self, l, r, k):
65        return self._getFirstKSum(self.roots[l], self.roots[r+1], 0, self.n-1, k)
66
67class Solution:
68    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
69        n = len(nums)
70        divided = []
71        prefix = [0]
72        new_nums = []
73        for i, num in enumerate(nums):
74            divided.append(num // k)
75            prefix.append(prefix[-1] + divided[-1])
76            new_nums.append((divided[-1], i))
77        compressed = {}
78        uncompressed = [0] * n
79        new_nums.sort()
80        index = 0
81        for num, i in new_nums:
82            compressed[(num, i)] = index
83            uncompressed[index] = num
84            index += 1
85        
86        same_group = [0] * n
87        i = 0
88        group = 0
89        while i < n:
90            rem = nums[i] % k
91            while i < n and nums[i] % k == rem:
92                same_group[i] = group
93                i += 1
94            group += 1
95
96        segTree = PSegmentTree(index, divided, compressed)
97        ret = []
98        for l, r in queries:
99            if same_group[l] != same_group[r]:
100                ret.append(-1)
101                continue
102            
103            window = r - l + 1
104            half = window // 2
105            if window % 2:
106                med = segTree.getKthSmallest(l, r, half + 1)
107                median = uncompressed[med]
108                leftSum = segTree.getFirstKSum(l, r, half + 1)
109                remSum = (prefix[r + 1] - prefix[l]) - leftSum
110                ret.append((median * (half + 1) - leftSum) + (remSum - median * half))
111            else:
112                median_l = uncompressed[segTree.getKthSmallest(l, r, half)]
113                median_r = uncompressed[segTree.getKthSmallest(l, r, half + 1)]
114                median = (median_l + median_r) // 2
115                leftSum = segTree.getFirstKSum(l, r, half)
116                remSum = (prefix[r + 1] - prefix[l]) - leftSum
117                ret.append((median * half - leftSum) + (remSum - median * half))
118        
119        return ret