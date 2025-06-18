# Last updated: 18/6/2025, 10:54:20 pm
N = 10**9
class Node:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.left = None
        self.right = None
        self.max = 0
        self.lazy = 0

class MyCalendarTwo:
    def __init__(self):
        self.node = Node(0, N)
    
    def push(self, node):
        mid = (node.l + node.r) // 2
        if node.left == None:
            node.left = Node(node.l, mid)
        if node.right == None:
            node.right = Node(mid+1, node.r)
        
        if node.lazy:
            node.left.max += node.lazy
            node.right.max += node.lazy
            node.left.lazy += node.lazy
            node.right.lazy += node.lazy
            node.lazy = 0
    
    def update(self, node, s, e):
        if node.r < s or node.l > e: return 

        if node.l >= s and node.r <= e:
            node.max += 1
            node.lazy += 1
            return
            
        self.push(node)

        self.update(node.left, s, e)
        self.update(node.right, s, e)
        
        node.max = max(node.left.max, node.right.max)

    def query(self, node, s, e):
        if node == None or node.r < s or node.l > e: return 0 

        if node.l >= s and node.r  <= e:
            return node.max
        
        self.push(node)

        return max(self.query(node.left, s, e), self.query(node.right, s, e)) + node.lazy

    def book(self, startTime: int, endTime: int) -> bool:
        if self.query(self.node, startTime, endTime-1) >= 2: return False

        self.update(self.node, startTime, endTime-1)
        return True

# [[],[28,46],[9,21],[21,39], [37,48],[38,50],[22,39], [45,50],[1,12], [40,50],[31,44]]
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)