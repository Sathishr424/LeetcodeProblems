# Last updated: 9/4/2025, 10:26:11 pm
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ret = ''

        l = 0
        r = 0

        while word1 and word2:
            if word1[0] > word2[0]:
                ret += word1[0]
                word1 = word1[1:]
            elif word1[0] < word2[0]:
                ret += word2[0]
                word2 = word2[1:]
            else:
                if word1 > word2:
                    ret += word1[0]
                    word1 = word1[1:]
                else:
                    ret += word2[0]
                    word2 = word2[1:]
        
        return ret + word1 + word2


