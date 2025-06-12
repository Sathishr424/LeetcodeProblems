# Last updated: 12/6/2025, 5:46:59 am
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None: return []
        ret = []
        stack = [root]

        while stack:
            s = stack.pop()
            ret.append(s.val)
            for i in range(len(s.children)-1, -1, -1):
                stack.append(s.children[i])

        return ret