# Last updated: 12/6/2025, 5:43:49 am
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def rec(node, sum):
            if node == None: return sum < limit
            left = rec(node.left, sum+node.val)
            right = rec(node.right, sum+node.val)

            if left: 
                node.left = None
                return node.right == None or right
            if right: 
                node.right = None
                return node.left == None or left

            return False
        if rec(root, 0): return None
        return root