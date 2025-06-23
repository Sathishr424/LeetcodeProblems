# Last updated: 24/6/2025, 2:32:01 am
cmin = lambda x, y: x if x < y else y
inf = float('inf')
class Node:
    def __init__(self, val):
        self.val = val
        self.childs = [None for _ in range(26)]

class Trie:
    def __init__(self):
        self.node = Node(inf)
    
    def insert(self, val):
        node = self.node
        for i in range(len(val)):
            a = ord(val[i]) - 97
            if node.childs[a] == None:
                node.childs[a] = Node(val[i])
            node = node.childs[a]
    
    def getMatch(self, word, index):
        node = self.node
        for i in range(index, len(word)):
            a = ord(word[i]) - 97
            if node.childs[a] == None:
                return i - index
            node = node.childs[a]
        return len(word) - index
    
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(words)
        m = len(target)

        trie = Trie()
        
        for i, word in enumerate(words):
            trie.insert(word)
        
        dp = [inf] * (m + 1)
        dp[0] = 0
        for i in range(1, m+1):
            cnt = trie.getMatch(target, i-1)
            # print(target[:i], cnt)
            for j in range(i, i+cnt):
                dp[j] = min(dp[j], dp[i - 1] + 1)
            # print(dp)
        # print(dp)
        return -1 if dp[-1] == inf else dp[-1]