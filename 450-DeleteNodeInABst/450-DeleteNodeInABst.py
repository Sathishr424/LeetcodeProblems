# Last updated: 12/6/2025, 5:49:18 am
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        def findRightMost(node):
            while node.right:
                node = node.right
            return node
        
        stack = [(None, root, '')]  # (parent, current node, direction)

        while stack:
            parent, node, direction = stack.pop()

            if node.val == key:
                # Case 1: Node has both children
                if node.left and node.right:
                    rNode = findRightMost(node.left)
                    rNode.right = node.right
                    if parent is None:
                        return node.left
                    if direction == 'L':
                        parent.left = node.left
                    else:
                        parent.right = node.left  # Fixed the typo here
                # Case 2: Node has only one child (left or right)
                elif node.left or node.right:
                    child = node.left if node.left else node.right
                    if parent is None:
                        return child  # Return new root if deleting root
                    if direction == 'L':
                        parent.left = child
                    else:
                        parent.right = child
                # Case 3: Node has no children (leaf node)
                else:
                    if parent:
                        if direction == 'L':
                            parent.left = None
                        else:
                            parent.right = None
                    else:
                        return None  # If the root is being deleted and has no children
                return root  # Return updated tree
            
            # Continue searching
            if node.left:
                stack.append((node, node.left, 'L'))
            if node.right:
                stack.append((node, node.right, 'R'))
        
        return root
