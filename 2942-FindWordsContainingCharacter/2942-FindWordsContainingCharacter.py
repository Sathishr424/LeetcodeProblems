# Last updated: 24/5/2025, 3:54:21 pm
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ret = []
        for i, word in enumerate(words):
            for char in word:
                if char == x:
                    ret.append(i)
                    break
        
        return ret