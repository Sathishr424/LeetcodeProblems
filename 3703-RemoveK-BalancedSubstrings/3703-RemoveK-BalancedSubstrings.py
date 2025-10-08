# Last updated: 8/10/2025, 10:11:35 pm
class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        # rel = ['(', ')']
        # s = [rel[random.randrange(2)] for _ in range(10 ** 5)]
        n = len(s)
        stack = []
        close = 0
        for i in range(n):
            if s[i] == '(':
                if close:
                    stack.append([')', close])
                    close = 0
                if stack and stack[-1][0] == '(':
                    stack[-1][1] += 1
                else:
                    stack.append(['(', 1])
            else:
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

        if close:
            stack.append([')', close])
        
        ret = ''
        for p, cnt in stack:
            ret += p * cnt
        
        return ret