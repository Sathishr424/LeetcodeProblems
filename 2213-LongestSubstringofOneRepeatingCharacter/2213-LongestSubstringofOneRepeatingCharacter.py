# Last updated: 8/13/2026, 1:39:45 PM
1class Node:
2    __slots__ = ('left', 'right', 'best')
3
4    def __init__(self, left=0, right=0, best=0):
5        self.left = left
6        self.right = right
7        self.best = best
8
9class SegmentTree:
10    def __init__(self, nums):
11        self.nums = nums
12        self.n = len(nums)
13
14        self.tree = [None for _ in range(self.n * 4)]
15        self.build(0, 0, self.n-1)
16
17    def mergeNodes(self, left, right, l, mid, r):
18        node = Node(left.left, right.right, max(left.best, right.best))
19
20        if self.nums[mid] == self.nums[mid + 1]:
21            node.best = max(node.best, left.right + right.left)
22
23            if left.left == (mid - l + 1):
24                node.left = left.left + right.left
25            if right.left == (r - mid):
26                node.right = right.left + left.right
27
28        return node
29
30    def build(self, index, l, r):
31        if l == r:
32            self.tree[index] = Node(1, 1, 1)
33            return self.tree[index]
34
35        mid = (l + r) // 2
36
37        left = self.build(index * 2 + 1, l, mid)
38        right = self.build(index * 2 + 2, mid + 1, r)
39
40        self.tree[index] = self.mergeNodes(left, right, l, mid, r)
41        return self.tree[index]
42
43    def update(self, index, l, r, pos):
44        if l == r:
45            return self.tree[index]
46
47        mid = (l + r) // 2
48
49        if pos <= mid:
50            left = self.update(index * 2 + 1, l, mid, pos)
51            right = self.tree[index * 2 + 2]
52        else:
53            left = self.tree[index * 2 + 1]
54            right = self.update(index * 2 + 2, mid + 1, r, pos)
55
56        self.tree[index] = self.mergeNodes(left, right, l, mid, r)
57        return self.tree[index]
58
59class Solution:
60    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
61        n = len(s)
62        k = len(queryCharacters)
63        s = list(s)
64
65        ans = []
66        segTree = SegmentTree(s)
67
68        for i in range(k):
69            index = queryIndices[i]
70            s[index] = queryCharacters[i]
71
72            node = segTree.update(0, 0, n-1, index)
73            ans.append(node.best)
74
75        return ans