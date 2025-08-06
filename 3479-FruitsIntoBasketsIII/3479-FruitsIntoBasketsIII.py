# Last updated: 6/8/2025, 11:19:01 am
class SegmentTree:
    def __init__(self, baskets):
        self.baskets = baskets
        self.n = len(baskets)
        self.tree = [0] * (self.n * 4)

        self.build(0, self.n-1, 0)
    
    def build(self, l, r, index):
        if l == r:
            self.tree[index] = self.baskets[l]
            return self.tree[index]
        
        mid = (l + r) // 2
        left = self.build(l, mid, index * 2 + 1)
        right = self.build(mid + 1, r, index * 2 + 2)

        self.tree[index] = max(left, right)
        return self.tree[index]
    
    def query(self, l, r, index, capacity):
        if self.tree[index] < capacity:
            return False
        
        if l == r:
            self.tree[index] = 0
            return True
        
        mid = (l + r) // 2

        canPlace = self.query(l, mid, index * 2 + 1, capacity)
        if not canPlace:
            canPlace = self.query(mid + 1, r, index * 2 + 2, capacity)

        self.tree[index] = max(self.tree[index * 2 + 1], self.tree[index * 2 + 2])
        return canPlace

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)

        segTree = SegmentTree(baskets)

        placed = 0
        for f in fruits:
            if segTree.query(0, n-1, 0, f): placed += 1
        
        return n - placed