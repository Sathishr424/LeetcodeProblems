# Last updated: 12/6/2025, 5:36:04 am
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