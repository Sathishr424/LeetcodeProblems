# Last updated: 5/10/2025, 8:46:52 am
class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        n = len(s)

        open = 0
        prefix_o = [0] * n
        for i in range(n):
            if s[i] == '(':
                open += 1
            else:
                open = 0
            prefix_o[i] = open
        change = False
        i = 0
        open = 0
        stack = []
        while i < n:
            if i + k <= n:
                if open >= k and s[i] == ')':
                    j = i
                    while j < n and s[j] == ')':
                        j += 1
                    can = min(open, j - i) // k * k
                    if can >= k:
                        change = True
                        i += can
                        while can:
                            stack.pop()
                            can -= 1
                        open = 0
                        if stack:
                            open = prefix_o[stack[-1]]
                        continue
                
            if s[i] == '(':
                open += 1
            else:
                open = 0
            
            stack.append(i)
            # print(stack, open)
            i += 1

        if change:
            return self.removeSubstring(''.join([s[i] for i in stack]), k)
        else:
            return ''.join([s[i] for i in stack])