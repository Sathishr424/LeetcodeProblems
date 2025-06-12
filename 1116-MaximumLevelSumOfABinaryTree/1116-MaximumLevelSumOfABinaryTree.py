# Last updated: 12/6/2025, 5:44:01 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_sum = float('-inf')
        max_level = 1
        level = 1
        queue = deque([root])

        while queue:
            level_sum = sum(node.val for node in queue)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return max_level
