# Last updated: 1/7/2025, 7:10:16 am
class Solution:
    def possibleStringCount(self, word: str) -> int:
        ret = 1
        
        prev = 0
        cnt = 0
        for i in range(1, len(word)):
            if word[i] == word[prev]:
                cnt += 1
            else:
                ret += cnt
                cnt = 0
                prev = i
        
        return ret + cnt