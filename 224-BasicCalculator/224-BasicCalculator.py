# Last updated: 12/6/2025, 5:51:28 am
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        def rec(i):
            op = 1
            ans = 0
            curr = 0
            while i < n:
                if s[i] == '(':
                    curr, i = rec(i+1)
                    ans += curr * op
                    curr = 0
                elif s[i] == ')':
                    ans += curr * op
                    return [ans, i]
                elif s[i] == '-':
                    ans += curr * op
                    op = -1
                    curr = 0
                elif s[i] == '+':
                    ans += curr * op
                    op = 1
                    curr = 0
                elif s[i] != ' ':
                    curr = curr * 10 + int(s[i])
                i += 1
            ans += curr * op
            return [ans, i]
        return rec(0)[0]


