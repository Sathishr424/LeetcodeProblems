# Last updated: 12/6/2025, 5:52:04 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.arr = deque([])
        def rec(node):
            if node == None: return
            rec(node.left)
            self.arr.append(node.val)
            rec(node.right)
        rec(root)
        # print(self.arr)

    def next(self) -> int:
        return self.arr.popleft()

    def hasNext(self) -> bool:
        return len(self.arr) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()