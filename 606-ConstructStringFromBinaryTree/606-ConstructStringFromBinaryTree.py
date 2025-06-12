# Last updated: 12/6/2025, 5:48:06 am
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ret = ""
        def rec(node):
            nonlocal ret
            if node == None: return
            ret += str(node.val)
            if node.right or node.left:
                ret += '('
                rec(node.left)
                ret += ')'
            if node.right:
                ret += '('
                rec(node.right)
                ret += ')'
        rec(root)
        return ret
            