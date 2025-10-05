# Last updated: 5/10/2025, 11:27:10 am
class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        n = len(s)
        stack = []

        open = 0
        close = 0
        for i in range(n):
            if s[i] == '(':
                if close:
                    stack.append([')', close])
                    close = 0
                open += 1
                if stack and stack[-1][0] == '(':
                    stack[-1][1] += 1
                else:
                    stack.append(['(', 1])
            else:
                open = 0
                close += 1
                if close == k and stack and stack[-1][0] == '(' and stack[-1][1] >= k:
                    stack[-1][1] -= k
                    if stack[-1][1] == 0:
                        stack.pop()
                        if stack:
                            close = stack.pop()[1]
                        else:
                            close = 0
                    else:
                        close = 0
            # print(stack, open, close, s[i])
        if close:
            stack.append([')', close])
        
        ret = ''
        for p, cnt in stack:
            ret += p * cnt
        
        return ret