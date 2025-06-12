# Last updated: 12/6/2025, 5:38:51 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start = None
        dest = None

        stack = [[root, '']]

        while stack:
            s, d = stack.pop()
            if s.val == startValue: 
                start = d
                if dest != None: break
            elif s.val == destValue: 
                dest = d
                if start != None: break
            if s.left:
                stack.append([s.left, d+'L'])
            if s.right:
                stack.append([s.right, d+'R'])
        ret = ''
        left = 0
        while left < min(len(start), len(dest)) and start[left] == dest[left]:
            left += 1
        for i in range(left, len(start)):
            ret += 'U'
        for i in range(left, len(dest)):
            ret += dest[i]
        return ret