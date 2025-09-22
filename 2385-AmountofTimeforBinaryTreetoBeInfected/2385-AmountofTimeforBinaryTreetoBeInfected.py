# Last updated: 22/9/2025, 10:32:14 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parents = defaultdict(None)
        nodes = defaultdict(None)

        def dfs(node, par):
            if node == None: return
            nodes[node.val] = node
            parents[node.val] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)
        stack = [start]

        minutes = 0
        infected = defaultdict(int)
        infected[start] = 1
        while stack:
            new_stack = []
            # print(minutes, dict(infected))
            while stack:
                val = stack.pop()

                node = nodes[val]
                parent = parents[val]

                if node.left and infected[node.left.val] == 0:
                    infected[node.left.val] = 1
                    new_stack.append(node.left.val)
                if node.right and infected[node.right.val] == 0:
                    infected[node.right.val] = 1
                    new_stack.append(node.right.val)

                if parent and infected[parent.val] == 0:
                    infected[parent.val] = 1
                    new_stack.append(parent.val)

            minutes += 1
            stack = new_stack
        # print(infected)
        return minutes - 1