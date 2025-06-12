# Last updated: 12/6/2025, 5:44:15 am
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = [(root, 0)]
        while stack:
            node, val = stack.pop()
            if node.left == None and node.right == None:
                ans += (val*2) + node.val
            if node.left: stack.append((node.left, (val*2) + node.val))
            if node.right: stack.append((node.right, (val*2) + node.val))
        return ans


            