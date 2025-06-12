# Last updated: 12/6/2025, 5:49:19 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def rec(node):
            if node == None: return ''
            if node.left and node.right:
                return f"{node.val}({rec(node.left)})({rec(node.right)})"
            elif node.left:
                return f"{node.val}({rec(node.left)})()"
            elif node.right:
                return f"{node.val}()({rec(node.right)})"
            else:
                return f"{node.val}()()"
        return rec(root)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        # 5(2)(6(2)(1()(5)))
        n = len(data)
        if n == 0: return None
        def rec(i):
            curr = ''
            while i < n:
                if data[i] == '(':
                    tree = TreeNode(int(curr))
                    tree.left, i = rec(i+1)
                    tree.right, i = rec(i+1)
                    return [tree, i+1]
                elif data[i] == ')':
                    if len(curr) > 0:
                        return [TreeNode(int(curr)), i+1]
                    else: return [None, i+1]
                else:
                    curr += data[i]
                i += 1
            return [TreeNode(int(curr)), i]
        return rec(0)[0]

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans