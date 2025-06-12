# Last updated: 12/6/2025, 5:51:38 am
class Node:
    def __init__(self, val):
        self.val = val
        self.word = False
        self.childs = []

class WordDictionary:
    def __init__(self):
        self.node = Node(-1)

    def addWord(self, word: str) -> None:
        node = self.node
        for i in range(len(word)):
            found = False
            for child in node.childs:
                if child.val == word[i]:
                    node = child
                    found = True
                    break
            if not found:
                node.childs.append(Node(word[i]))
                node = node.childs[-1]
        node.word = True
    
    def _search(self, word, node, index=0):
        for i in range(index, len(word)):
            if word[i] == '.':
                for child in node.childs:
                    if self._search(word, child, i+1): return True
                return False
            else:
                found = False
                for child in node.childs:
                    if child.val == word[i]:
                        node = child
                        found = True
                        break
                if not found: return False
        return node.word

    def search(self, word: str) -> bool:
        return self._search(word, self.node)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)