# Last updated: 12/25/2025, 7:08:37 PM
class Node:
    def __init__(self, l, r):
        self.score = 0
        self.left = None
        self.right = None
        self.l = l
        self.r = r

class SegmentTree:
    def __init__(self, n):
        self.node = Node(1, n)
    
    def processLazy(self, node, l, mid, r):
        if node.left == None:
            node.left = Node(l, mid)
        if node.right == None:
            node.right = Node(mid +1, r)
        
    def update(self, node, l, r, index, score):
        if l == r:
            node.score = score
            return
        
        mid = (l + r) // 2
        self.processLazy(node, l, mid, r)
        if index <= mid:
            self.update(node.left, l, mid, index, score)
        else:
            self.update(node.right, mid + 1, r, index, score)
        node.score = node.left.score + node.right.score
    
    def query(self, node, l, r, left, right):
        if l > right or r < left:
            return 0

        if l >= left and r <= right:
            return node.score

        mid = (l + r) // 2
        self.processLazy(node, l, mid, r)

        return self.query(node.left, l, mid, left, right) + self.query(node.right, mid + 1, r, left, right)

class ExamTracker:
    def __init__(self):
        self.n = 10 ** 9
        self.segTree = SegmentTree(self.n)

    def record(self, time: int, score: int) -> None:
        return self.segTree.update(self.segTree.node, 1, self.n, time, score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        return self.segTree.query(self.segTree.node, 1, self.n, startTime, endTime)

# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)