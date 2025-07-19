# Last updated: 19/7/2025, 2:15:59 pm
class Node:
    def __init__(self):
        self.childs = [None] * 27
        self.is_end = False

class Trie:
    def __init__(self):
        self.mainNode = Node()
    
    def insert(self, folder):
        node = self.mainNode
        for char in folder:
            if char == '/':
                if node.is_end: return
                a = 26
            else:
                a = ord(char) - 97
            if node.childs[a] == None:
                node.childs[a] = Node()
            node = node.childs[a]
        node.is_end = True
        node.childs[26] = None
    
    def getAllMainFolders(self, node, s, ret):
        if node.is_end:
            ret.append(s)
        for child in range(26):
            if node.childs[child] == None: continue
            self.getAllMainFolders(node.childs[child], s + chr(child + 97), ret)
        if node.childs[26] != None:
            self.getAllMainFolders(node.childs[26], s + '/', ret)

class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        n = len(folders)
        trie = Trie()
        for folder in folders:
            trie.insert(folder)
        
        ret = []
        trie.getAllMainFolders(trie.mainNode, '', ret)
        return ret