# Last updated: 12/6/2025, 5:44:17 am
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ret = ""
        open = 0
        for p in s:
            if p == '(':
                open += 1
                if open > 1: ret += p
            else:
                open -= 1
                if open: ret += p
        return ret