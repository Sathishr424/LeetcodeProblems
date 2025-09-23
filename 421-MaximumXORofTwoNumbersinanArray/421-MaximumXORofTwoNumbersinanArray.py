# Last updated: 23/9/2025, 2:34:27 pm
class Node:
    def __init__(self):
        self.bits = [None, None]

class Trie:
    def __init__(self):
        self.node = Node()
    
    def insert(self, num):
        node = self.node
        bits = [0] * 32
        index = 31
        while num:
            bits[index] = num & 1
            num >>= 1
            index -= 1
        
        for bit in bits:
            if node.bits[bit] == None:
                node.bits[bit] = Node()
            
            node = node.bits[bit]
    
    def getMax(self, node, bit, num, x):
        if bit == -1: return x

        is_setbit = num & (1 << bit) > 0
        opp = 0 if is_setbit else 1
        curr = 1 if is_setbit else 0

        if node.bits[opp]:
            return self.getMax(node.bits[opp], bit - 1, num, x + (1 << bit))
        
        return self.getMax(node.bits[curr], bit - 1, num, x)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()

        for num in nums:
            trie.insert(num)

        maxi = 0
        for num in nums:
            maxi = max(maxi, trie.getMax(trie.node, 31, num, 0))
        
        return maxi
