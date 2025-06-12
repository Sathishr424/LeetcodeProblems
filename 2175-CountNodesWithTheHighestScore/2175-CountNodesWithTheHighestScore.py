# Last updated: 12/6/2025, 5:39:02 am
from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.l_cnt = 0
        self.r_cnt = 0

class Solution:
    def countHighestScoreNodes(self, parents) -> int:
        arr = [Node(i) for i in range(len(parents))]
        root = None
        for i, p in enumerate(parents):
            if p == -1:
                root = arr[i]
                continue
            if arr[p].left == None:
                arr[p].left = arr[i]
            else:
                arr[p].right = arr[i]
        
        ret = defaultdict(int)

        def rec(node):
            if node == None: return 0
            left = rec(node.left)
            right = rec(node.right)

            node.l_cnt = left
            node.r_cnt = right

            return left + right + 1
        
        maxi = 0
        def rec2(node, par=0):
            nonlocal maxi
            if node == None: return
            val = 1
            if par: val *= par
            if node.l_cnt: val *= node.l_cnt
            if node.r_cnt: val *= node.r_cnt
            ret[val] += 1
            maxi = max(val, maxi)
            rec2(node.left, node.r_cnt+par+1)
            rec2(node.right, node.l_cnt+par+1)
        
        rec(root)
        rec2(root)
        return ret[maxi]