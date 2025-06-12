# Last updated: 12/6/2025, 5:47:02 am
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(x, y, w):
            # print(x, y, w)
            if is_uniform(x, y, w):
                return Node(grid[y][x], True)
            w = w//2
            topLeft = helper(x, y, w)
            topRight = helper(x+w, y, w)
            bottomLeft = helper(x, y+w, w)
            bottomRight = helper(x+w, y+w, w)
            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
        
        def is_uniform(x, y, w):
            # print(x, y)
            val = grid[y][x]
            for i in range(y, y+w):
                for j in range(x, x+w):
                    if grid[i][j] != val: return False
            
            return True
        
        return helper(0, 0, len(grid))