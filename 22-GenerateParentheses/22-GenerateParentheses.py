# Last updated: 12/6/2025, 5:55:02 am
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def rec(st, open, close):
            if open == close and open == n: return ret.append(st)
            if open < n:
                rec(st+'(', open+1, close)
            if open-close > 0:
                rec(st+')', open, close+1)
        rec('(', 1, 0)
        return ret