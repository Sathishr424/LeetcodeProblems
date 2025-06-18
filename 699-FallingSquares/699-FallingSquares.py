# Last updated: 18/6/2025, 11:16:47 pm
N = 101000000
class SegNode:
    def __init__(self, l, r):
        self.max = 0
        self.l = l
        self.r = r
        self.lazy = 0
        self.left = None
        self.right = None

class SegTree:
    def __init__(self):
        self.node = SegNode(0, N)
    
    def push(self, node):
        mid = (node.l + node.r) // 2
        if node.left == None:
            node.left = SegNode(node.l, mid)
        if node.right == None:
            node.right = SegNode(mid+1, node.r)
        
        if node.lazy:
            node.left.max = node.lazy
            node.right.max = node.lazy
            node.left.lazy = node.lazy
            node.right.lazy = node.lazy
            node.lazy = 0

    def query(self, node, x, y):
        if node.r < x or node.l > y: return 0
        
        if node.l >= x and node.r <= y:
            return node.max
        
        self.push(node)

        return max(self.query(node.left, x, y), self.query(node.right, x, y))
    
    def update(self, node, x, y, h):
        if node.r < x or node.l > y: return
        if node.l >= x and node.r <= y:
            node.lazy = h
            node.max = h
            return
        
        self.push(node)
        self.update(node.left, x, y, h)
        self.update(node.right, x, y, h)

        node.max = max(node.left.max, node.right.max)

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        tree = SegTree()
        ret = []

        for x, y in positions:
            h = tree.query(tree.node, x, x + y - 1)
            tree.update(tree.node, x, x + y - 1, h + y)
            ret.append(tree.node.max)

        return ret