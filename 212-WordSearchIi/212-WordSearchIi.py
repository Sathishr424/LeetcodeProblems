# Last updated: 12/6/2025, 5:51:40 am
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores complete word at leaf nodes

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word  # Mark end of word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = Trie()
        
        # Insert words into Trie
        for word in words:
            trie.insert(word)

        res = set()

        def dfs(i, j, node):
            if board[i][j] not in node.children:
                return
            
            char = board[i][j]
            next_node = node.children[char]
            
            if next_node.word:
                res.add(next_node.word)
                next_node.word = None  # Avoid duplicates

            board[i][j] = '#'  # Mark visited
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] in next_node.children:
                    dfs(ni, nj, next_node)
            
            board[i][j] = char  # Restore cell
            
            # Optimization: Remove leaf nodes from Trie
            # if not next_node.children:
            #     del node.children[char]

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root)

        return list(res)
