# Last updated: 12/6/2025, 5:42:41 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.hash = {}
        def rec(node, val):
            if node == None: return

            node.val = val
            self.hash[node.val] = 1
            rec(node.left, node.val * 2 + 1)
            rec(node.right, node.val * 2 + 2)
        self.root = rec(root, 0)

    def find(self, target: int) -> bool:
        return target in self.hash


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)