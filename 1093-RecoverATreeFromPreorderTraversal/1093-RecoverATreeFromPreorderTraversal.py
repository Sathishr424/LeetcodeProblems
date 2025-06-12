# Last updated: 12/6/2025, 5:44:09 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, t: str) -> Optional[TreeNode]:
        num = ''
        index = 0
        while index < len(t) and t[index] != '-':
            index += 1

        head = TreeNode(int(t[0:index]))
        levels = {1: head}
        left = index
        while index < len(t):
            if t[index] != '-':
                depth = index - left

                start = index
                while index < len(t) and t[index] != '-': index += 1

                num = int(t[start:index])
                left = index

                node = levels[depth]
                if node.left == None:
                    node.left = TreeNode(num)
                    levels[depth+1] = node.left
                else:
                    node.right = TreeNode(num)
                    levels[depth+1] = node.right
            index += 1
        
        return head