# Last updated: 27/11/2025, 1:23:00 pm
1mod = 10**9 + 7
2
3class Node:
4    def __init__(self):
5        self.sum = 0
6        self.x = 0
7        self.n = 0
8
9    def __repr__(self):
10        return f"{self.sum}, {self.x}, {self.n}"
11
12class SegmentTree:
13    def __init__(self, nums):
14        self.nums = nums
15        self.n = len(nums)
16        self.tree = [Node() for _ in range(self.n * 4)]
17
18        self.build(0, self.n-1, 0)
19    
20    def build(self, l, r, index):
21        if l == r:
22            self.tree[index].sum += self.nums[l]
23            if self.nums[l] > 0:
24                self.tree[index].n += 1
25                self.tree[index].x = self.nums[l]
26            return self.tree[index]
27        
28        mid = (l + r) // 2
29        left = self.build(l, mid, index * 2 + 1)
30        right = self.build(mid + 1, r, index * 2 + 2)
31
32        self.tree[index].sum = left.sum + right.sum
33        x = (left.x * pow(10, right.n, mod) % mod) + right.x
34        x %= mod
35        self.tree[index].x = x
36        self.tree[index].n = left.n + right.n
37        return self.tree[index]
38    
39    def query(self, l, r, index, left, right):
40        if l > right or r < left:
41            return Node()
42        
43        # print((left, right), l, r, index)
44        if l >= left and r <= right:
45            return self.tree[index]
46        
47        mid = (l + r) // 2
48        left_node = self.query(l, mid, index * 2 + 1, left, right)
49        right_node = self.query(mid + 1, r, index * 2 + 2, left, right)
50
51        new_node = Node()
52        x = (left_node.x * pow(10, right_node.n, mod) % mod) + right_node.x
53        x %= mod
54        new_node.sum = left_node.sum + right_node.sum
55        new_node.x = x
56        new_node.n = left_node.n + right_node.n
57        return new_node
58
59class Solution:
60    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
61        n = len(s)
62
63        nums = [int(d) for d in s]
64        ret = []
65        
66        segTree = SegmentTree(nums)
67        # print(segTree.tree)
68
69        for l, r in queries:
70            node = segTree.query(0, n-1, 0, l, r)
71            # print((l, r), node)
72            ret.append(node.sum * node.x % mod)
73
74        return ret