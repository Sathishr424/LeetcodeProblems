# Last updated: 12/6/2025, 5:47:12 am
alpSmall = list('abcdefghijklmnopqrstuvwxyz')
alpCaps = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

class Solution:
    def checkIfThere(self,char):
        for i in range(len(alpCaps)):
            if char == alpCaps[i]: return alpSmall[i]
        return str(char)
        
    def toLowerCase(self, str: str) -> str:
        ret = ""
        for i in str:
            ret += self.checkIfThere(i)
        return ret