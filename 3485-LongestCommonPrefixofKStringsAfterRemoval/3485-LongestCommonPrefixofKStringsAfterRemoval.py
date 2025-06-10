# Last updated: 11/6/2025, 12:17:03 am
class Node:
    def __init__(self):
        self.cnt = 0
        self.childs = {}

class Trie:
    def __init__(self):
        self.node = Node()
        self.memo = {}
    
    def insert(self, val):
        node = self.node
        for char in val:
            a = ord(char) - 97
            if a not in node.childs:
                node.childs[a] = Node()
            node = node.childs[a]
            if node in self.memo:
                del self.memo[node]
            node.cnt += 1

    def remove(self, val):
        node = self.node
        for char in val:
            a = ord(char) - 97
            node = node.childs[a]
            if node in self.memo:
                del self.memo[node]
            node.cnt -= 1

    def getLongestCommonPrefix(self, node, k):
        if node.cnt > 0 and node in self.memo:
            return self.memo[node]
        ans = 0
        for child in node.childs:
            child = node.childs[child]
            if child.cnt >= k:
                ans = max(ans, self.getLongestCommonPrefix(child, k) + 1)
        self.memo[node] = ans
        return ans

class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        n = len(words)

        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ret = []
        for word in words:
            trie.remove(word)
            ret.append(trie.getLongestCommonPrefix(trie.node, k))
            trie.insert(word)
        
        return ret