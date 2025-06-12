# Last updated: 12/6/2025, 5:47:00 am
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None: return 0
        def rec(node):
            cnt = 0
            for child in node.children:
                cnt = max(cnt, rec(child))
            return cnt+1
        
        return rec(root)
        