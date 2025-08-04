# Last updated: 4/8/2025, 11:55:48 pm
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def rec(rem, opened, s):
            if rem == 0:
                if opened == 0:
                    ret.append(s)
                return
            
            if opened < rem - 1:
                rec(rem - 1, opened + 1, s + '(')
            if opened:
                rec(rem - 1, opened - 1, s + ')')
        
        rec(n * 2, 0, '')
        return ret