# Last updated: 12/6/2025, 5:48:41 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        ret = []
        stack = deque([(root, 0)])
        while stack:
            node, level = stack.popleft()
            if level < len(ret):
                ret[level] = max(ret[level], node.val)
            else:
                ret.append(node.val)
            if node.left != None: stack.append((node.left, level+1))
            if node.right != None: stack.append((node.right, level+1))
        
        return ret
