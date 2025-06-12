# Last updated: 12/6/2025, 5:53:11 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexes = {}
        for i, num in enumerate(inorder): indexes[num] = i

        def buildTree(left, right, pre_index):
            num = preorder[pre_index]
            index = indexes[num]

            node = TreeNode(num)

            diff = index-left
            if index > left:
                node.left = buildTree(left, index-1, pre_index+1)
            if right > index:
                node.right = buildTree(index+1, right, pre_index+diff+1)

            return node
        
        return buildTree(0, len(preorder)-1, 0)