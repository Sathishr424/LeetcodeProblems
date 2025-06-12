# Last updated: 12/6/2025, 5:43:16 am
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        vis = {}
        for i in range(n):
            if leftChild[i] != -1:
                vis[leftChild[i]] = 1
            if rightChild[i] != -1:
                vis[rightChild[i]] = 1
        parent = None
        for i in range(n):
            if i not in vis:
                if parent != None: return False
                parent = i
        vis = {}
        def rec(i):
            if i == -1: return True
            if i in vis: return False
            vis[i] = 1
            if not rec(leftChild[i]): return False
            if not rec(rightChild[i]): return False
            return True
        
        return parent != None and rec(parent) and len(vis) == n