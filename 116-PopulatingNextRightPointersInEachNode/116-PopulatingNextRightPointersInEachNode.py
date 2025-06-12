# Last updated: 12/6/2025, 5:52:55 am
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None or root.left == None: return root
        stack = deque([root.left, root.right])

        while stack:
            cnt = len(stack)
            prev = stack.popleft()
            if prev.left:
                stack.append(prev.left)
                stack.append(prev.right)
            for _ in range(cnt-1):
                curr = stack.popleft()
                prev.next = curr
                if curr.left:
                    stack.append(curr.left)
                    stack.append(curr.right)
                prev = curr
        return root