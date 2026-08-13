# Last updated: 8/13/2026, 1:36:30 PM
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
43    def update(self, index, l, r, left, right):
44        if r < left or l > right:
45            return self.tree[index]
46
47        if l >= left and r <= right:
48            return self.tree[index]
49
50        mid = (l + r) // 2
51        left_node = self.update(index * 2 + 1, l, mid, left, right)
52        right_node = self.update(index * 2 + 2, mid + 1, r, left, right)
53
54        self.tree[index] = self.mergeNodes(left_node, right_node, l, mid, r)
55        return self.tree[index]
56
57class Solution:
58    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
59        n = len(s)
60        k = len(queryCharacters)
61        s = list(s)
62
63        ans = []
64        segTree = SegmentTree(s)
65
66        for i in range(k):
67            index = queryIndices[i]
68            s[index] = queryCharacters[i]
69
70            node = segTree.update(0, 0, n-1, index, index)
71            ans.append(node.best)
72
73        return ans