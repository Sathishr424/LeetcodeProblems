# Last updated: 24/5/2025, 3:56:59 pm
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ret = []
        for i, word in enumerate(words):
            m = len(word)
            index = random.randrange(m)
            for j in range(index, index+m):
                if word[j  % m] == x:
                    ret.append(i)
                    break
        
        return ret