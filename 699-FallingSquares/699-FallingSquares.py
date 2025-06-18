# Last updated: 19/6/2025, 2:08:16 am
N = 101000000
cmax = lambda x, y: x if x > y else y

class Node:
    def __init__(self):
        self.lazy = 0
        self.max = 0

class SegmentTree:
    def __init__(self, n):
        self.tree = [Node() for _ in range(n * 4)]
    
    def processLazy(self, index, lazy):
        if lazy:
            left = index * 2 + 1
            right = index * 2 + 2
            self.tree[left].lazy = lazy
            self.tree[right].lazy = lazy
            self.tree[left].max = lazy
            self.tree[right].max = lazy
            self.tree[index].lazy = 0
    
    def query(self, l, r, index, left, right):
        if l > right or r < left: return 0

        if l >= left and r <= right:
            return self.tree[index].max
        
        self.processLazy(index, self.tree[index].lazy)
        mid = (l + r) // 2
        return max(self.query(l, mid, index * 2 + 1, left, right), self.query(mid + 1, r, index * 2 + 2, left, right))

    def update(self, l, r, index, left, right, h):
        if l > right or r < left: return

        if l >= left and r <= right:
            self.tree[index].lazy = h
            self.tree[index].max = h
            return
        
        self.processLazy(index, self.tree[index].lazy)
        mid = (l + r) // 2
        self.update(l, mid, index * 2 + 1, left, right, h)
        self.update(mid+1, r, index * 2 + 2, left, right, h)

        self.tree[index].max = max(self.tree[index * 2 + 1].max, self.tree[index * 2 + 2].max)

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        pos = {}
        for x, y in positions:
            pos[x] = 1
            pos[x+y-1] = 1
        
        keys = sorted(pos.keys())
        index = 0
        compressed = {}
        for x in keys:
            compressed[x] = index
            index += 1

        tree = SegmentTree(index)
        ret = []

        for x_, y_ in positions:
            x = compressed[x_]
            y = compressed[x_+y_-1]

            h = tree.query(0, index-1, 0, x, y)

            tree.update(0, index-1, 0, x, y, h + y_)
            ret.append(tree.tree[0].max)

        return ret