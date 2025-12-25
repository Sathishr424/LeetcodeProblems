# Last updated: 12/25/2025, 7:08:00 PM
mod = 10**9 + 7

class Node:
    def __init__(self):
        self.sum = 0
        self.x = 0
        self.n = 0

    def __repr__(self):
        return f"{self.sum}, {self.x}, {self.n}"

class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.tree = [Node() for _ in range(self.n * 4)]

        self.build(0, self.n-1, 0)
    
    def build(self, l, r, index):
        if l == r:
            self.tree[index].sum += self.nums[l]
            if self.nums[l] > 0:
                self.tree[index].n += 1
                self.tree[index].x = self.nums[l]
            return self.tree[index]
        
        mid = (l + r) // 2
        left = self.build(l, mid, index * 2 + 1)
        right = self.build(mid + 1, r, index * 2 + 2)

        self.tree[index].sum = left.sum + right.sum
        x = (left.x * pow(10, right.n, mod) % mod) + right.x
        x %= mod
        self.tree[index].x = x
        self.tree[index].n = left.n + right.n
        return self.tree[index]
    
    def query(self, l, r, index, left, right):
        if l > right or r < left:
            return Node()
        
        # print((left, right), l, r, index)
        if l >= left and r <= right:
            return self.tree[index]
        
        mid = (l + r) // 2
        left_node = self.query(l, mid, index * 2 + 1, left, right)
        right_node = self.query(mid + 1, r, index * 2 + 2, left, right)

        new_node = Node()
        x = (left_node.x * pow(10, right_node.n, mod) % mod) + right_node.x
        x %= mod
        new_node.sum = left_node.sum + right_node.sum
        new_node.x = x
        new_node.n = left_node.n + right_node.n
        return new_node

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        nums = [int(d) for d in s]
        ret = []
        
        segTree = SegmentTree(nums)
        # print(segTree.tree)

        for l, r in queries:
            node = segTree.query(0, n-1, 0, l, r)
            # print((l, r), node)
            ret.append(node.sum * node.x % mod)

        return ret