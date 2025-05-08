# Last updated: 9/5/2025, 1:55:28 am
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
            else:
                num >>= 1
                index = self.check(num, node.one)
                if index != -1: return index

                return self.check(num, node.zero)
            num >>= 1
        
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
        seen = {}

        start_mask = 1 << n
        for i in range(m):
            mask = start_mask
            for j in range(n):
                if grid[i][j]:
                    mask += 1 << (n-j-1)
            if mask == start_mask: return [i]
            trie.insert(mask, i)
            seen[mask] = i
            # print(format(mask, '010b'), mask)
        
        # 0 1 1 0 1 0
        # 000, 010, 011, 111, 101, 100, 110

        for mask in seen:
            index = trie.check(mask, trie.node)
            if index != -1: return sorted([seen[mask], index])
        
        return []