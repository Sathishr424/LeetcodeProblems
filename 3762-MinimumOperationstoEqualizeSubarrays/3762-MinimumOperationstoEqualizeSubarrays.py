# Last updated: 3/12/2025, 3:38:08 pm
1import sys
2sys.setrecursionlimit(1 << 20)
3
4class PSegmentTree:
5    def __init__(self, m, nums, compressed):
6        # m = number of distinct compressed positions
7        self.m = m
8        # index 0 = null / empty node
9        self.lefts = [0]
10        self.rights = [0]
11        self.cnts = [0]
12        self.sums = [0]
13        self.roots = [0]  # root for prefix 0
14        # build versions by updating from previous root
15        for i, num in enumerate(nums):
16            pos = compressed[(num, i)]
17            new_root = self._update(self.roots[-1], 0, self.m - 1, pos, num)
18            self.roots.append(new_root)
19
20    def _new_node(self, l=0, r=0, cnt=0, s=0):
21        self.lefts.append(l)
22        self.rights.append(r)
23        self.cnts.append(cnt)
24        self.sums.append(s)
25        return len(self.lefts) - 1
26
27    def _update(self, node, Lb, Rb, pos, val):
28        L, R, CNT, SUM = self.lefts, self.rights, self.cnts, self.sums
29        idx = self._new_node(L[node], R[node], CNT[node], SUM[node])
30        if Lb == Rb:
31            # leaf
32            self.cnts[idx] = CNT[node] + 1
33            self.sums[idx] = SUM[node] + val
34            return idx
35        mid = (Lb + Rb) // 2
36        if pos <= mid:
37            left_child = self._update(L[node], Lb, mid, pos, val)
38            self.lefts[idx] = left_child
39        else:
40            right_child = self._update(R[node], mid + 1, Rb, pos, val)
41            self.rights[idx] = right_child
42        self.cnts[idx] = self.cnts[self.lefts[idx]] + self.cnts[self.rights[idx]]
43        self.sums[idx] = self.sums[self.lefts[idx]] + self.sums[self.rights[idx]]
44        return idx
45
46    def _kth(self, left_root, right_root, Lb, Rb, k):
47        L, R, CNT = self.lefts, self.rights, self.cnts
48        if Lb == Rb:
49            return Lb
50        mid = (Lb + Rb) // 2
51        left_count = CNT[L[right_root]] - CNT[L[left_root]]
52        if left_count >= k:
53            return self._kth(L[left_root], L[right_root], Lb, mid, k)
54        return self._kth(R[left_root], R[right_root], mid + 1, Rb, k - left_count)
55
56    def _first_k_sum(self, left_root, right_root, Lb, Rb, k):
57        L, R, CNT, SUM = self.lefts, self.rights, self.cnts, self.sums
58        if Lb == Rb:
59            return SUM[right_root] - SUM[left_root]
60        mid = (Lb + Rb) // 2
61        left_count = CNT[L[right_root]] - CNT[L[left_root]]
62        if left_count >= k:
63            return self._first_k_sum(L[left_root], L[right_root], Lb, mid, k)
64        left_sum = SUM[L[right_root]] - SUM[L[left_root]]
65        return left_sum + self._first_k_sum(R[left_root], R[right_root], mid + 1, Rb, k - left_count)
66
67    # wrappers that mirror your earlier API
68    def getKthSmallest(self, l_idx, r_idx, k):
69        # your code used roots[l], roots[r+1] — so pass the indices appropriately when calling
70        return self._kth(self.roots[l_idx], self.roots[r_idx + 1], 0, self.m - 1, k)
71
72    def getFirstKSum(self, l_idx, r_idx, k):
73        return self._first_k_sum(self.roots[l_idx], self.roots[r_idx + 1], 0, self.m - 1, k)
74
75
76class Solution:
77    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
78        n = len(nums)
79        divided = []
80        prefix = [0]
81        new_nums = []
82        for i, num in enumerate(nums):
83            divided.append(num // k)
84            prefix.append(prefix[-1] + divided[-1])
85            new_nums.append((divided[-1], i))
86        compressed = {}
87        uncompressed = [0] * n
88        new_nums.sort()
89        index = 0
90        for num, i in new_nums:
91            compressed[(num, i)] = index
92            uncompressed[index] = num
93            index += 1
94        
95        same_group = [0] * n
96        i = 0
97        group = 0
98        while i < n:
99            rem = nums[i] % k
100            while i < n and nums[i] % k == rem:
101                same_group[i] = group
102                i += 1
103            group += 1
104
105        segTree = PSegmentTree(index, divided, compressed)
106        ret = []
107        for l, r in queries:
108            if same_group[l] != same_group[r]:
109                ret.append(-1)
110                continue
111            
112            window = r - l + 1
113            half = window // 2
114            if window % 2:
115                med = segTree.getKthSmallest(l, r, half + 1)
116                median = uncompressed[med]
117                leftSum = segTree.getFirstKSum(l, r, half + 1)
118                remSum = (prefix[r + 1] - prefix[l]) - leftSum
119                ret.append((median * (half + 1) - leftSum) + (remSum - median * half))
120            else:
121                median_l = uncompressed[segTree.getKthSmallest(l, r, half)]
122                median_r = uncompressed[segTree.getKthSmallest(l, r, half + 1)]
123                median = (median_l + median_r) // 2
124                leftSum = segTree.getFirstKSum(l, r, half)
125                remSum = (prefix[r + 1] - prefix[l]) - leftSum
126                ret.append((median * half - leftSum) + (remSum - median * half))
127        
128        return ret