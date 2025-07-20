# Last updated: 20/7/2025, 10:07:42 pm
class Node:
    def __init__(self):
        self.childs = {}
        self.cache = ''

class Trie:
    def __init__(self):
        self.mainNode = Node()
        self.cached = defaultdict(int)
    
    def insert(self, path):
        node = self.mainNode

        for folder in path:
            if folder not in node.childs:
                node.childs[folder] = Node()
            node = node.childs[folder]
    
    def cache(self, node):
        s = ''
        for folder in sorted(node.childs.keys()):
            s += folder + '/' + self.cache(node.childs[folder])
            s += '-'
        node.cache = s
        self.cached[s] += 1
        return s
    
    def getValidPaths(self, node, s, ret):
        ret.append(s[:])
        for folder in node.childs:
            child_node = node.childs[folder]
            if self.cached[child_node.cache] <= 1:
                s.append(folder)
                self.getValidPaths(child_node, s, ret)
                s.pop()

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        ret = []

        trie = Trie()

        for path in paths:
            trie.insert(path)
        trie.cache(trie.mainNode)

        trie.cached[''] = 0
        trie.getValidPaths(trie.mainNode, [], ret)
        return ret[1:]