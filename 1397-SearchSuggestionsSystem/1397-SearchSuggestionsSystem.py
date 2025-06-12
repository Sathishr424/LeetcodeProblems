# Last updated: 12/6/2025, 5:42:38 am
class Node:
    def __init__(self, val):
        self.val = val
        self.childs = []
        self.word = False

class Trie:
    def __init__(self):
        self.node = Node(-1)

    def _insert(self, node, val, index):
        if index == len(val):
            node.word = True
            return 
        for child in node.childs:
            if child.val == val[index]:
                return self._insert(child, val, index+1)
        node.childs.append(Node(val[index]))
        return self._insert(node.childs[-1], val, index+1)

    def insert(self, val):
        self._insert(self.node, val, 0)
    
    def _startsWith(self, node, val, index):
        if index == len(val): return node
        for child in node.childs:
            if child.val == val[index]:
                return self._startsWith(child, val, index+1)
        return None

    def starstWith(self, val):
        node = self._startsWith(self.node, val, 0)
        if node == None: return []

        stack = [(val, node)]
        ret = []
        while stack:
            val, node = heapq.heappop(stack)
            if node.word: 
                ret.append(val)
                if len(ret) == 3: break
            for child in node.childs:
                heapq.heappush(stack, (val + child.val, child))
        return ret
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()

        for product in products:
            trie.insert(product)

        ret = []
        curr = ''
        for i in range(len(searchWord)):
            ret.append(trie.starstWith(searchWord[:i+1]))

        return ret