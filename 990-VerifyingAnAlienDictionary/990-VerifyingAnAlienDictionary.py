# Last updated: 12/6/2025, 5:44:55 am
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hash = {}
        for i in range(len(order)):
            hash[order[i]] = i
        
        for i in range(1, len(words)):
            for j, w in enumerate(words[i]):
                if j == len(words[i-1]) or hash[words[i-1][j]] < hash[w]: break
                elif hash[words[i-1][j]] > hash[w]: return False
                elif j == len(words[i])-1 and words[i-1][j] == w and len(words[i-1]) > len(words[i]): return False
        
        return True
