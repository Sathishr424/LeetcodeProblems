# Last updated: 8/13/2026, 1:33:07 PM
1class Node:
2    def __init__(self, left=0, right=0, best=0):
3        self.left = left
4        self.right = right
5        self.best = best
6
7class SegmentTree:
8    def __init__(self, nums):
9        self.nums = nums
10        self.n = len(nums)
11        self.m = self.n * 4
12
13        self.indexes = [-1 for _ in range(self.n)]
14        self.tree = [None for _ in range(self.m)]
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
33            self.indexes[l] = index
34            return self.tree[index]
35
36        mid = (l + r) // 2
37
38        left = self.build(index * 2 + 1, l, mid)
39        right = self.build(index * 2 + 2, mid + 1, r)
40
41        self.tree[index] = self.mergeNodes(left, right, l, mid, r)
42        return self.tree[index]
43
44    def update(self, index, l, r, left, right):
45        if r < left or l > right:
46            return self.tree[index]
47
48        if l >= left and r <= right:
49            return self.tree[index]
50
51        mid = (l + r) // 2
52        left_node = self.update(index * 2 + 1, l, mid, left, right)
53        right_node = self.update(index * 2 + 2, mid + 1, r, left, right)
54
55        self.tree[index] = self.mergeNodes(left_node, right_node, l, mid, r)
56        return self.tree[index]
57
58class Solution:
59    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
60        n = len(s)
61        k = len(queryCharacters)
62        s = list(s)
63
64        ans = []
65        segTree = SegmentTree(s)
66
67        for i in range(k):
68            index = queryIndices[i]
69            s[index] = queryCharacters[i]
70
71            node = segTree.update(0, 0, n-1, index, index)
72            ans.append(node.best)
73
74        return ans
75