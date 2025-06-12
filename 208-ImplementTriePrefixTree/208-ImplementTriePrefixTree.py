# Last updated: 12/6/2025, 5:51:44 am
class Node:
    def __init__(self, val):
        self.val = val
        self.childs = []
        self.word = False

class Trie:
    def __init__(self):
        self.node = Node(-1)

    def insert(self, word: str) -> None:
        node = self.node
        for i in range(len(word)):
            found = False
            for child in node.childs:
                if child.val == word[i]:
                    found = True
                    node = child
                    break
            if not found:
                node.childs.append(Node(word[i]))
                node = node.childs[-1]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.node
        for i in range(len(word)):
            found = False
            for child in node.childs:
                if child.val == word[i]:
                    found = True
                    node = child
                    break
            if not found: return False
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.node
        for i in range(len(prefix)):
            found = False
            for child in node.childs:
                if child.val == prefix[i]:
                    found = True
                    node = child
                    break
            if not found: return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)