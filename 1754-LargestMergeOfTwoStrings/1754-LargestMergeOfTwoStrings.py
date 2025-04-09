# Last updated: 9/4/2025, 10:27:50 pm
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ret = ''

        while word1 and word2:
            if word1 > word2:
                ret += word1[0]
                word1 = word1[1:]
            else:
                ret += word2[0]
                word2 = word2[1:]
        
        return ret + word1 + word2


