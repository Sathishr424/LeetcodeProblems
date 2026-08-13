# Last updated: 8/13/2026, 1:30:10 PM
1from typing import *
2from collections import defaultdict, deque, Counter
3from functools import lru_cache, cache
4from itertools import accumulate, combinations, permutations, product
5from bisect import bisect_left, bisect_right, insort
6from heapq import *
7from math import *
8from string import ascii_lowercase, ascii_uppercase
9from sortedcontainers import SortedList
10import random
11import re
12
13class Node:
14    def __init__(self, left=0, right=0, best=0):
15        self.left = left
16        self.right = right
17        self.best = best
18
19class SegmentTree:
20    def __init__(self, nums):
21        self.nums = nums
22        self.n = len(nums)
23        self.m = self.n * 4
24
25        self.indexes = [-1 for _ in range(self.n)]
26        self.tree = [None for _ in range(self.m)]
27        self.build(0, 0, self.n-1)
28
29    def mergeNodes(self, left, right, l, mid, r):
30        node = Node(left.left, right.right, max(left.best, right.best))
31
32        if self.nums[mid] == self.nums[mid + 1]:
33            node.best = max(node.best, left.right + right.left)
34
35            if left.left == (mid - l + 1):
36                node.left = left.left + right.left
37            if right.left == (r - mid):
38                node.right = right.left + left.right
39
40        return node
41
42    def build(self, index, l, r):
43        if l == r:
44            self.tree[index] = Node(1, 1, 1)
45            self.indexes[l] = index
46            return self.tree[index]
47
48        mid = (l + r) // 2
49
50        left = self.build(index * 2 + 1, l, mid)
51        right = self.build(index * 2 + 2, mid + 1, r)
52
53        self.tree[index] = self.mergeNodes(left, right, l, mid, r)
54        return self.tree[index]
55
56    def update(self, index, l, r, left, right):
57        if r < left or l > right:
58            return self.tree[index]
59
60        if l >= left and r <= right:
61            return self.tree[index]
62
63        mid = (l + r) // 2
64        left_node = self.update(index * 2 + 1, l, mid, left, right)
65        right_node = self.update(index * 2 + 2, mid + 1, r, left, right)
66
67        self.tree[index] = self.mergeNodes(left_node, right_node, l, mid, r)
68        return self.tree[index]
69
70class Solution:
71    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
72        n = len(s)
73        k = len(queryCharacters)
74        s = list(s)
75
76        ans = []
77        segTree = SegmentTree(s)
78
79        for i in range(k):
80            index = queryIndices[i]
81            s[index] = queryCharacters[i]
82
83            node = segTree.update(0, 0, n-1, index, index)
84            ans.append(node.best)
85
86        return ans
87