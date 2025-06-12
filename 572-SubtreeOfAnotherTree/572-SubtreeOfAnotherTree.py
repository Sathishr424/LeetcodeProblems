# Last updated: 12/6/2025, 5:48:17 am
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        match = ""
        def helper(node):
            nonlocal match
            if node == None: 
                match += "None,"
                return
            helper(node.left)
            helper(node.right)
            match += str(node.val) + ","
        helper(subRoot)

        found = False
        def rec(node):
            nonlocal found
            if node == None: return "None,"
            left = rec(node.left)
            right = rec(node.right)
            s = left + right + str(node.val) + ","
            if s == match: found = True
            return s

        return rec(root) and found