# Last updated: 19/7/2025, 2:21:09 pm
class Node:
    def __init__(self):
        self.childs = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.mainNode = Node()
    
    def insert(self, folder):
        node = self.mainNode
        for char in folder:
            if char == '/' and node.is_end: return
            if char not in node.childs:
                node.childs[char] = Node()
            node = node.childs[char]
        node.is_end = True
        if '/' in node.childs:
            del node.childs['/']
    
    def getAllMainFolders(self, node, s, ret):
        if node.is_end: ret.append(s)
        for char in node.childs:
            if node.childs[char] == None: continue
            self.getAllMainFolders(node.childs[char], s + char, ret)

class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        n = len(folders)
        trie = Trie()
        for folder in folders:
            trie.insert(folder)
        
        ret = []
        trie.getAllMainFolders(trie.mainNode, '', ret)
        return ret