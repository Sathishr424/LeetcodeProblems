# Last updated: 12/6/2025, 5:38:21 am
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def rec(node):
            nonlocal ret
            if node == None: return [0, 0]
            left, left_cnt = rec(node.left)
            right, right_cnt = rec(node.right)
            _sum = left+right+node.val
            cnt = left_cnt+right_cnt+1
            ret += _sum//cnt == node.val
            return [_sum, cnt]
        rec(root)
        return ret