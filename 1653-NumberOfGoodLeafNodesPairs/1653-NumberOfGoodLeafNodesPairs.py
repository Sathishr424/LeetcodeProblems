# Last updated: 12/6/2025, 5:41:04 am
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> list:
        self.res = 0  
        
        def dfs(node) -> list:
            if not node: return []
            if not node.left and not node.right: return [1]

            left_list = dfs(node.left)
            right_list = dfs(node.right)
            self.res += sum(l+r <= distance for l in left_list for r in right_list)
            return [1+item for item in left_list+right_list]
        
        dfs(root)
        return self.res 