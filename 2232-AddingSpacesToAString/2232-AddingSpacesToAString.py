# Last updated: 12/6/2025, 5:38:48 am
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ret = []
        index = 0
        n = len(spaces)
        for i in range(len(s)):
            if index < n and i == spaces[index]:
                ret.append(' ')
                index += 1
            ret.append(s[i])
        
        return ''.join(ret)