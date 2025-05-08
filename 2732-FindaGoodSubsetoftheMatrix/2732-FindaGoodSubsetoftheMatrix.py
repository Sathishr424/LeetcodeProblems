# Last updated: 9/5/2025, 1:59:05 am
class Node:
    def __init__(self):
        self.one = None
        self.zero = None
        self.index = -1

class Trie:
    def __init__(self):
        self.node = Node()
    
    def check(self, num, node):
        if node == None: return -1

        while num != 1:
            if num & 1:
                if not node.zero: return -1
                node = node.zero
                num >>= 1
            else:
                num >>= 1
                index = self.check(num, node.one)
                if index != -1: return index

                return self.check(num, node.zero)
        
        return node.index

    def insert(self, num, index):
        node = self.node
        while num != 1:
            if num & 1:
                if node.one == None:
                    node.one = Node()
                node = node.one
            else:
                if node.zero == None:
                    node.zero = Node()
                node = node.zero
            num >>= 1
        node.index = index

class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        trie = Trie()
        start_mask = 1 << n

        for i in range(m):
            mask = start_mask

            for j in range(n):
                mask += grid[i][j] << (n-j-1)
            
            if mask == start_mask: return [i]

            index = trie.check(mask, trie.node)
            if index != -1: return [index, i]

            trie.insert(mask, i)
        
        return []