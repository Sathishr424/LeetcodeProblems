# Last updated: 11/6/2025, 12:45:28 am
class Node:
    def __init__(self):
        self.cnt = 0
        self.childs = {}

class Trie:
    def __init__(self):
        self.node = Node()
        self.largest = 0
        self.second_largest = 0
        self.largest_start = ''
    
    def calcSecondLargest(self, node, k):
        ans = 0
        for child in node.childs:
            if node.childs[child].cnt >= k:
                ans = max(ans, self.calcSecondLargest(node.childs[child], k) + 1)
        return ans

    def insert(self, val, k):
        node = self.node
        p = 0
        word = ''
        for char in val:
            a = ord(char) - 97
            if a not in node.childs:
                node.childs[a] = Node()
            node = node.childs[a]
            node.cnt += 1
            if node.cnt >= k:
                word += char
                p += 1
        
        if p > self.largest:
            self.largest = p
            self.largest_start = word
    
    def remove(self, val):
        node = self.node
        for char in val:
            a = ord(char) - 97
            node = node.childs[a]
            node.cnt -= 1

class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        n = len(words)

        trie = Trie()
        for word in words:
            trie.insert(word, k)
        
        trie.remove(trie.largest_start)
        second_largest = trie.calcSecondLargest(trie.node, k)

        ret = []
        for word in words:
            if word[:len(trie.largest_start)] == trie.largest_start:
                ret.append(second_largest)
            else:
                ret.append(trie.largest)
        
        return ret