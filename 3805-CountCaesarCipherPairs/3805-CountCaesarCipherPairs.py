# Last updated: 1/16/2026, 1:13:53 PM
1class Node:
2    def __init__(self):
3        self.cnt = 0
4        self.childs = [None] * 26
5
6class Trie:
7    def __init__(self):
8        self.node = Node()
9
10    def insert(self, word):
11        node = self.node
12        prev = word[0]
13        for i in range(len(word)):
14            d = (word[i] - prev) % 26
15            if node.childs[d] == None:
16                node.childs[d] = Node()
17            node = node.childs[d]
18            node.cnt += 1
19
20    def count(self, word):
21        node = self.node
22        maxCnt = inf
23        prev = word[0]
24        for i in range(len(word)):
25            d = (word[i] - prev) % 26
26            if node.childs[d] == None:
27                return 0
28            node = node.childs[d]
29            maxCnt = min(maxCnt, node.cnt)
30
31        return maxCnt
32
33class Solution:
34    def countPairs(self, words: List[str]) -> int:
35        n = len(words)
36        m = len(words[0])
37
38        trie = Trie()
39        ans = 0
40
41        for i, word in enumerate(words):
42            word = [ord(c) - ord('a') for c in word]
43            ans += trie.count(word)
44            trie.insert(word)
45
46        return ans