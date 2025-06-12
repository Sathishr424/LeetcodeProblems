# Last updated: 12/6/2025, 5:41:33 am
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        n = len(sentence)
        
        i = 0
        res = 1
        prev = ''
        for char in sentence:
            if char == searchWord[i]:
                if i == 0 and prev != ' ' and prev != '':
                    prev = char
                    continue
                i += 1
                if i == len(searchWord): return res
            else:
                i = 0
                if char == ' ' and prev != ' ': res += 1
            prev = char
        
        return -1
