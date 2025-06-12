# Last updated: 12/6/2025, 5:34:02 am
class Solution:
    def reverseDegree(self, s: str) -> int:
        ret = 0

        for i, char in enumerate(s):
            ret += (26 - (ord(char) - 97)) * (i+1)
            

        return ret