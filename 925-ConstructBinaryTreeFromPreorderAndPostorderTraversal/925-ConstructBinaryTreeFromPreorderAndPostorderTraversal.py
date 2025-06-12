# Last updated: 12/6/2025, 5:45:34 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indexes = {}
        for i, num in enumerate(postorder): indexes[num] = i
        def buildTree(left, right, pre_index):
            num = postorder[right]
            node = TreeNode(num)

            if right > left:
                pre_index += 1
                index = indexes[preorder[pre_index]]
                
                node.left = buildTree(left, index, pre_index)

                diff = index-left
                left += diff+1
                right -= 1

                if right >= left:
                    node.right = buildTree(left, right, pre_index+diff+1)
            
            return node
        return buildTree(0, len(preorder)-1, 0)

        
        
