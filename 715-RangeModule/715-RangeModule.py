# Last updated: 19/6/2025, 12:06:58 am
N = 10**9
cmax = lambda x, y: x if x > y else y
class SegNode:
    def __init__(self, l, r):
        self.max = 0
        self.l = l
        self.r = r
        self.lazy = -1
        self.left = None
        self.right = None

class SegTree:
    def __init__(self):
        self.node = SegNode(0, N)
    
    def remove(self, node, s, e):
        if node.r < s or node.l > e: return
        if node.l >= s and node.r <= e:
            node.lazy = 0
            node.max = 0
            return
        
        self.push(node)
        self.remove(node.left, s, e)
        self.remove(node.right, s, e)

        node.max = min(node.left.max, node.right.max)
    
    def push(self, node):
        mid = (node.l + node.r) // 2
        if node.left == None:
            node.left = SegNode(node.l, mid)
        if node.right == None:
            node.right = SegNode(mid+1, node.r)
        
        if node.lazy != -1:
            node.left.max = node.lazy
            node.right.max = node.lazy
            node.left.lazy = node.lazy
            node.right.lazy = node.lazy
            node.lazy = -1

    def query(self, node, s, e):
        if node.r < s or node.l > e: return True
        if node.l >= s and node.r <= e:
            return True if node.max >= 1 else False
        
        self.push(node)
        return self.query(node.left, s, e) and self.query(node.right, s, e)
    
    def add(self, node, s, e):
        if node.r < s or node.l > e: return
        if node.l >= s and node.r <= e:
            node.lazy = 1
            node.max = 1
            return
        
        self.push(node)
        self.add(node.left, s, e)
        self.add(node.right, s, e)

        node.max = min(node.left.max, node.right.max)
    
class RangeModule:
    def __init__(self):
        self.tree = SegTree()

    def addRange(self, left: int, right: int) -> None:
        self.tree.add(self.tree.node, left, right-1)

    def queryRange(self, left: int, right: int) -> bool:
        ans = self.tree.query(self.tree.node, left, right-1)
        return ans

    def removeRange(self, left: int, right: int) -> None:
        self.tree.remove(self.tree.node, left, right-1)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)