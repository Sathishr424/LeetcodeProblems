# Last updated: 12/6/2025, 5:36:42 am
class Solution:
    def finalString(self, s: str) -> str:
        ret = ''
        for char in s:
            if char == 'i':
                ret = ret[::-1]
            else:
                ret += char

        return ret