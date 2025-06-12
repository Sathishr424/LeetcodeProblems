# Last updated: 12/6/2025, 5:49:58 am
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}
        ignore = {}
        
        for i, w in enumerate(s):
            if w in ignore: continue
            if w in hash: 
                del hash[w]
                ignore[w] = 1
            else:
                hash[w] = i
        
        index = -1
        for k in hash:
            index = min(hash[k], index) if index != -1 else hash[k]
        
        return index
        
