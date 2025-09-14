# Last updated: 15/9/2025, 1:20:31 am
class Node:
    def __init__(self):
        self.childs = [None, None]

class Trie:
    def __init__(self):
        self.node = Node()
    
    def insert(self, bits):
        node = self.node
        for bit in bits:
            if node.childs[bit] == None:
                node.childs[bit] = Node()
            node = node.childs[bit]
    
    def check(self, node, bits, index):
        if index == 32:
            return 0
        
        bit = bits[index]
        flip_bit = (bit + 1) & 1
        if node.childs[flip_bit]:
            return self.check(node.childs[flip_bit], bits, index + 1) + (1 << (31 - index))
        return self.check(node.childs[bit], bits, index + 1)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # maxi = 2 ** 31 - 1
        # nums = [random.randrange(0, maxi + 1) for _ in range(2 * (10 ** 5))]
        if len(nums) < 2: return 0
        ans = 0
        nums.sort()
        trie = Trie()

        for i, num in enumerate(nums):
            bits = [0] * 32
            index = 31
            while num:
                bits[index] = num & 1
                num >>= 1
                index -= 1
            
            if i > 0:
                ans = max(trie.check(trie.node, bits, 0), ans)
            
            trie.insert(bits)
        
        return ans