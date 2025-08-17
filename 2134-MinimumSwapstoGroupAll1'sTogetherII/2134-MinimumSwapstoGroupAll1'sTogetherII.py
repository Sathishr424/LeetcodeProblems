# Last updated: 17/8/2025, 6:07:55 pm
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        n = len(startWords)
        m = len(targetWords)

        ret = 0
        there = set()
        for word in startWords:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            
            for a in range(26):
                if mask & (1 << a) == 0:
                    there.add(mask | (1 << a))

        for word in targetWords:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            if mask in there: ret += 1

        return ret
                    
            