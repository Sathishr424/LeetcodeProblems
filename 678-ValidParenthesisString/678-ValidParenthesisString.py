# Last updated: 17/5/2025, 5:05:44 pm
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        @cache
        def rec(index, open):
            if index == n: return open == 0
            if open < 0 or n-index < open: return False
            if s[index] == '(':
                return rec(index+1, open+1)
            elif s[index] == ')':
                return rec(index+1, open-1)
            else:
                return rec(index+1, open+1) or rec(index+1, open-1) or rec(index+1, open)
        
        return rec(0, 0)
            
