# Last updated: 12/6/2025, 5:52:17 am
class Solution:
    def reverseWords(self, s: str) -> str:
        s = ' ' + s + ' '
        n = len(s)
        ret = ''
        word = ''
        for i in range(n-2, -1, -1):
            if s[i] == ' ':
                if s[i+1] != ' ':
                    ret += word[::-1] + ' '
                    word = ''
            else:
                word += s[i]
        
        return ret[:-1]