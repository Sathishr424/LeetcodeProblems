# Last updated: 9/23/2026, 12:07:34 AM
1class SegmentTree:
2    def __init__(self, nums: List[int], k: int):
3        self.k = k
4        n = len(nums)
5        size = 2 << n.bit_length()
6
7        # tree[o] = pre + [mul]
8        self.tree = [[0] * (k + 1) for _ in range(size)]
9
10        self.build(nums, 1, 0, n - 1)
11
12    def makeLeaf(self, o: int, value: int) -> None:
13        info = [0] * (self.k + 1)
14        r = value % self.k
15        info[r] = 1
16        info[self.k] = r  # mul
17        self.tree[o] = info
18
19    def mergePre(self, left: List[int], right: List[int]) -> List[int]:
20        pre = [0] * (self.k + 1)
21
22        mul_L = left[self.k]
23        mul_R = right[self.k]
24
25        # Remainder of the product of the entire interval
26        pre[self.k] = (mul_L * mul_R) % self.k
27
28        # Case 1: Entirely within the left interval
29        for x in range(self.k):
30            pre[x] = left[x]
31
32        # Case 2: Contains the entire left interval, followed by a prefix of the right interval
33        for x in range(self.k):
34            pre[(mul_L * x) % self.k] += right[x]
35
36        return pre
37
38    def maintain(self, o: int) -> None:
39        self.tree[o] = self.mergePre(
40            self.tree[o * 2],
41            self.tree[o * 2 + 1],
42        )
43
44    def build(self, nums: List[int], o: int, l: int, r: int) -> None:
45        if l == r:
46            self.makeLeaf(o, nums[l])
47            return
48
49        m = (l + r) // 2
50        self.build(nums, o * 2, l, m)
51        self.build(nums, o * 2 + 1, m + 1, r)
52        self.maintain(o)
53
54    def update(self, o: int, l: int, r: int, index: int, value: int) -> None:
55        if l == r:
56            self.makeLeaf(o, value)
57            return
58
59        m = (l + r) // 2
60        if index <= m:
61            self.update(o * 2, l, m, index, value)
62        else:
63            self.update(o * 2 + 1, m + 1, r, index, value)
64
65        self.maintain(o)
66
67    def query(self, o: int, l: int, r: int, L: int, R: int) -> List[int]:
68        if L <= l and r <= R:
69            return self.tree[o]
70
71        m = (l + r) // 2
72        if R <= m:
73            return self.query(o * 2, l, m, L, R)
74        if L > m:
75            return self.query(o * 2 + 1, m + 1, r, L, R)
76
77        left = self.query(o * 2, l, m, L, R)
78        right = self.query(o * 2 + 1, m + 1, r, L, R)
79        return self.mergePre(left, right)
80
81
82class Solution:
83    def resultArray(
84        self, nums: List[int], k: int, queries: List[List[int]]
85    ) -> List[int]:
86        n = len(nums)
87        seg = SegmentTree(nums, k)
88
89        ans = []
90        for index, value, start, x in queries:
91            seg.update(1, 0, n - 1, index, value)
92            pre = seg.query(1, 0, n - 1, start, n - 1)
93            ans.append(pre[x])
94
95        return ans