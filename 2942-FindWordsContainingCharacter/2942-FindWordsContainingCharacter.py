# Last updated: 24/5/2025, 3:56:21 pm
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ret = []
        for i, word in enumerate(words):
            index = random.randrange(len(word))
            for j in range(index, index+len(word)):
                if word[j  % len(word)] == x:
                    ret.append(i)
                    break
        
        return ret