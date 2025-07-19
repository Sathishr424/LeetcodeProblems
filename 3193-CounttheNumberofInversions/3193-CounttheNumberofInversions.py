# Last updated: 19/7/2025, 5:32:22 pm
class SegmentNode:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.left = None
        self.right = None
        self.track = False
        self.lazy = -1

class SegmentTree:
    def __init__(self, n):
        self.node = SegmentNode(0, n)
    
    def processLazy(self, node, mid):
        if node.left == None:
            node.left = SegmentNode(node.l, mid)
        if node.right == None:
            node.right = SegmentNode(mid + 1, node.r)
        
        if node.lazy != -1:
            node.left.track = node.lazy == 1
            node.right.track = node.lazy == 1
            node.left.lazy = node.lazy
            node.right.lazy = node.lazy
            node.lazy = -1
    
    def addRange(self, l, r, node):
        if node.l >= l and node.r <= r:
            node.track = True
            node.lazy = 1
            return
        
        mid = (node.l + node.r) // 2
        self.processLazy(node, mid)

        if l <= mid:
            self.addRange(l, r, node.left)
        if r > mid:
            self.addRange(l, r, node.right)
        
        node.track = node.left.track and node.right.track
    
    def removeRange(self, l, r, node):
        if node.l >= l and node.r <= r:
            node.track = False
            node.lazy = 0
            return
        
        mid = (node.l + node.r) // 2
        self.processLazy(node, mid)

        if l <= mid:
            self.removeRange(l, r, node.left)
        if r > mid:
            self.removeRange(l, r, node.right)
        
        node.track = node.left.track and node.right.track

    def queryRange(self, l, r, node):
        if node.l >= l and node.r <= r:
            return node.track
        
        mid = (node.l + node.r) // 2
        self.processLazy(node, mid)

        track = True
        if l <= mid:
            track = self.queryRange(l, r, node.left)
        if r > mid:
            track = track and self.queryRange(l, r, node.right)
        
        return track

N = 10**9
class RangeModule:
    def __init__(self):
        self.tree = SegmentTree(N)

    def addRange(self, left: int, right: int) -> None:
        self.tree.addRange(left, right-1, self.tree.node)

    def queryRange(self, left: int, right: int) -> bool:
        return self.tree.queryRange(left, right-1, self.tree.node)

    def removeRange(self, left: int, right: int) -> None:
        self.tree.removeRange(left, right-1, self.tree.node)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)