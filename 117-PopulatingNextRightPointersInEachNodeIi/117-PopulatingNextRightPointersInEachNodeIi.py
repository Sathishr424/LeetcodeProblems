# Last updated: 12/6/2025, 5:52:54 am
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None: return None
        levels = []

        def helper(node, level):
            if node == None: return
            if len(levels) == level:
                levels.append(node)
            else:
                levels[level].next = node
                levels[level] = node
            helper(node.left, level+1)
            helper(node.right, level+1)
        helper(root, 0)
        
        return root
