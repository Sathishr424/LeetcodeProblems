# Last updated: 12/6/2025, 5:45:04 am
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ret = 0
        def rec(node):
            nonlocal ret
            if node == None: return
            if node.val >= low:
                rec(node.left)
                if node.val <= high: ret += node.val
            if node.val < high:
                rec(node.right)
        rec(root)
        return ret

            