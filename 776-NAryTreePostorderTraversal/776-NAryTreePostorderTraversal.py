# Last updated: 12/6/2025, 5:46:58 am
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None: return []
        ret = deque([])

        stack = [root]

        while stack:
            s = stack.pop()
            ret.appendleft(s.val)
            for child in s.children:
                stack.append(child)

        return ret
        