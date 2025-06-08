# Last updated: 8/6/2025, 9:38:49 pm
class Node:
    def __init__(self):
        self.childs = [None for _ in range(10)]

class Trie:
    def __init__(self):
        self.node = Node()
    
    def insert_(self, val, node):
        if val == 0: return node
        
        curr = val % 10
        node = self.insert_(val // 10, node)

        if node.childs[curr] == None:
            node.childs[curr] = Node()
        
        return node.childs[curr]
    
    def insert(self, val):
        node = self.node
        for i in range(len(val)):
            if node.childs[val[i]] != None:
                node = node.childs[val[i]]
            else:
                node.childs[val[i]] = Node()
                node = node.childs[val[i]]
    
    def getAll(self, node, curr, ret):
        for child in range(10):
            if node.childs[child] != None:
                ret.append(curr + child)
                self.getAll(node.childs[child], (curr + child) * 10, ret)

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ret = []
        trie = Trie()
        for i in range(1, n+1):
            trie.insert_(i, trie.node)
        
        trie.getAll(trie.node, 0, ret)
        
        return ret