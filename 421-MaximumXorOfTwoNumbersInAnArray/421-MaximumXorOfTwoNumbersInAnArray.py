# Last updated: 12/6/2025, 5:49:35 am
class Node:
    def __init__(self):
        self.left = None
        self.right = None

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        main_node = Node()

        def insert(node, num, index):
            if index == -1: return
            if num >> index & 1:
                if not node.right: node.right = Node()
                insert(node.right, num, index-1)
            else:
                if not node.left: node.left = Node()
                insert(node.left, num, index-1)
            
        cnt = 0
        maxi = max(nums)
        while maxi:
            maxi >>= 1
            cnt += 1

        for num in nums:
            insert(main_node, num, cnt-1)
        
        def rec(node, num, final_num, index):
            if index == -1:
                return final_num
            
            val = num >> index & 1

            if val:
                if node.left:
                    return rec(node.left, num, final_num << 1 | 1, index-1)
                elif node.right:
                    return rec(node.right, num, final_num << 1, index-1)
            else:
                if node.right:
                    return rec(node.right, num, final_num << 1 | 1, index-1)
                elif node.left:
                    return rec(node.left, num, final_num << 1, index-1)
            return 0

        ans = 0
        for num in nums:
            ans = max(ans, rec(main_node, num, 0, cnt-1))
        
        return ans
        

