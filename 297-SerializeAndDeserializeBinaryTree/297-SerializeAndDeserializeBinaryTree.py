# Last updated: 12/6/2025, 5:50:46 am
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        def rec(node):
            if node == None: return ''
            # return f"{node.val}({rec(node.left)})({rec(node.right)})"
            if node.left or node.right:
                return f"{node.val}({rec(node.left)})({rec(node.right)})"
            else:
                return str(node.val)
        return rec(root)

    def deserialize(self, val: str) -> Optional[TreeNode]:
        def rec(index):
            curr = ''
            for i in range(index, len(val)):
                if val[i] == '(':
                    node = TreeNode(int(curr))
                    node.left, i = rec(i+1)
                    node.right, i = rec(i+1)
                    return [node, i+1]
                elif val[i] == ')':
                    if curr: return [TreeNode(int(curr)), i+1]
                    return [None, i+1]
                else:
                    curr += val[i]
            if curr: return [TreeNode(int(curr)), 0]
            return [None, 0]
        return rec(0)[0]
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))