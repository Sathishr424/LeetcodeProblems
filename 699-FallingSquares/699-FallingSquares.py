# Last updated: 19/6/2025, 2:14:34 am
N = 101000000
cmax = lambda x, y: x if x > y else y
class SegmentTree:
    def __init__(self, n):
        self.tree = [0] * (n * 4)
        self.lazy = [0] * (n * 4)
    
    def processLazy(self, index):
        lazy = self.lazy[index]
        if lazy:
            left = index * 2 + 1
            right = index * 2 + 2
            self.tree[left] = lazy
            self.tree[right] = lazy
            self.lazy[left] = lazy
            self.lazy[right] = lazy
            self.lazy[index] = 0
    
    def query(self, l, r, index, left, right):
        if l > right or r < left: return 0

        if l >= left and r <= right:
            return self.tree[index]
        
        self.processLazy(index)
        mid = (l + r) // 2
        return cmax(self.query(l, mid, index * 2 + 1, left, right), self.query(mid + 1, r, index * 2 + 2, left, right))

    def update(self, l, r, index, left, right, h):
        if l > right or r < left: return

        if l >= left and r <= right:
            self.lazy[index] = h
            self.tree[index] = h
            return
        
        self.processLazy(index)
        mid = (l + r) // 2
        self.update(l, mid, index * 2 + 1, left, right, h)
        self.update(mid+1, r, index * 2 + 2, left, right, h)

        self.tree[index] = cmax(self.tree[index * 2 + 1], self.tree[index * 2 + 2])

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
            ret.append(tree.tree[0])

        return ret