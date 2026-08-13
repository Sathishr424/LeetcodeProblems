# Last updated: 8/13/2026, 1:34:30 PM
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
13        self.tree = [None for _ in range(self.m)]
14        self.build(0, 0, self.n-1)
15
16    def mergeNodes(self, left, right, l, mid, r):
17        node = Node(left.left, right.right, max(left.best, right.best))
18
19        if self.nums[mid] == self.nums[mid + 1]:
20            node.best = max(node.best, left.right + right.left)
21
22            if left.left == (mid - l + 1):
23                node.left = left.left + right.left
24            if right.left == (r - mid):
25                node.right = right.left + left.right
26
27        return node
28
29    def build(self, index, l, r):
30        if l == r:
31            self.tree[index] = Node(1, 1, 1)
32            return self.tree[index]
33
34        mid = (l + r) // 2
35
36        left = self.build(index * 2 + 1, l, mid)
37        right = self.build(index * 2 + 2, mid + 1, r)
38
39        self.tree[index] = self.mergeNodes(left, right, l, mid, r)
40        return self.tree[index]
41
42    def update(self, index, l, r, left, right):
43        if r < left or l > right:
44            return self.tree[index]
45
46        if l >= left and r <= right:
47            return self.tree[index]
48
49        mid = (l + r) // 2
50        left_node = self.update(index * 2 + 1, l, mid, left, right)
51        right_node = self.update(index * 2 + 2, mid + 1, r, left, right)
52
53        self.tree[index] = self.mergeNodes(left_node, right_node, l, mid, r)
54        return self.tree[index]
55
56class Solution:
57    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
58        n = len(s)
59        k = len(queryCharacters)
60        s = list(s)
61
62        ans = []
63        segTree = SegmentTree(s)
64
65        for i in range(k):
66            index = queryIndices[i]
67            s[index] = queryCharacters[i]
68
69            node = segTree.update(0, 0, n-1, index, index)
70            ans.append(node.best)
71
72        return ans