# Last updated: 12/6/2025, 5:38:28 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hash = {}
        childs = {}

        for parent, child, is_left in descriptions:
            childs[child] = 1
            if parent in hash:
                if child in hash:
                    child = hash[child]
                else:
                    child = TreeNode(child)
                    hash[child.val] = child
                if is_left: hash[parent].left = child
                else: hash[parent].right = child
            else:
                hash[parent] = TreeNode(parent)
                if child in hash:
                    child = hash[child]
                else:
                    child = TreeNode(child)
                    hash[child.val] = child
                if is_left: hash[parent].left = child
                else: hash[parent].right = child
        for val in hash:
            if val not in childs: return hash[val]
        
        return None