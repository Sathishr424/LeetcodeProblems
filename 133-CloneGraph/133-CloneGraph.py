# Last updated: 12/6/2025, 5:52:36 am
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def copyNode(node):
            if node == None: return None
            if node in visited: return visited[node]
            copy_root = Node(node.val)
            visited[node] = copy_root
            for n in node.neighbors:
                copy_root.neighbors.append(copyNode(n))
            return copy_root
        
        return copyNode(node)