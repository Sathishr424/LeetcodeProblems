# Last updated: 8/6/2025, 9:28:20 pm
class Node:
    def __init__(self):
        self.childs = {}

class Trie:
    def __init__(self):
        self.node = Node()
    
    def insert(self, val):
        node = self.node
        for i in range(len(val)):
            if val[i] in node.childs:
                node = node.childs[val[i]]
            else:
                node.childs[val[i]] = Node()
                node = node.childs[val[i]]
    
    def getAll(self, node, curr, ret):
        for child in node.childs:
            ret.append(curr + int(child))
            self.getAll(node.childs[child], (curr + int(child)) * 10, ret)

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ret = []
        trie = Trie()
        for i in range(1, n+1):
            trie.insert(str(i))
        
        trie.getAll(trie.node, 0, ret)
        
        return ret


            
            