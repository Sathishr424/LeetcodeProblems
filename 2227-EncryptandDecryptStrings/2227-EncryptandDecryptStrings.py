# Last updated: 8/9/2025, 9:05:05 pm
class Node:
    def __init__(self):
        self.childs = [None for _ in range(26)]
        self.is_word = False

class Trie:
    def __init__(self):
        self.node = Node()

    def insert(self, word):
        node = self.node
        for char in word:
            a = ord(char) - ord('a')
            if node.childs[a] == None:
                node.childs[a] = Node()

            node = node.childs[a]
        node.is_word = True
    
class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self._decrypt.cache_clear()
        self.keys_dict = {}
        self.keys = keys
        for i, key in enumerate(keys):
            self.keys_dict[key] = i
        
        self.values = values
        self.values_dict = defaultdict(list)
        for i, val in enumerate(values):
            self.values_dict[val].append(i)

        self.dictionary = set(dictionary)
        self.trie = Trie()

        for word in dictionary:
            self.trie.insert(word)

    def encrypt(self, word1: str) -> str:
        ret = ''
        for char in word1:
            if char not in self.keys_dict: return ''
            ret += self.values[self.keys_dict[char]]
        return ret

    @cache
    def _decrypt(self, word, node):
        if len(word) == 0:
            return 1 if node.is_word else 0

        char = word[:2]
        ans = 0
        
        for i in self.values_dict[char]:
            a = ord(self.keys[i]) - ord('a')
            if node.childs[a] != None:
                ans += self._decrypt(word[2:], node.childs[a])

        return ans
    
    def decrypt(self, word2: str) -> int:
        return self._decrypt(word2, self.trie.node)

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)