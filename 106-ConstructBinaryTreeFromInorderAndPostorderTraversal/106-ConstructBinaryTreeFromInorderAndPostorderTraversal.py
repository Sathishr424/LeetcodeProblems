# Last updated: 12/6/2025, 5:53:10 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indexes = {}
        for i, num in enumerate(inorder): indexes[num] = i

        def buildTree(left, right, post_index):
            num = postorder[post_index]
            index = indexes[num]

            node = TreeNode(num)

            diff = right-index
            if index > left:
                node.left = buildTree(left, index-1, post_index-diff-1)
            if right > index:
                node.right = buildTree(index+1, right, post_index-1)
            
            return node
        
        return buildTree(0, len(inorder)-1, len(inorder)-1)