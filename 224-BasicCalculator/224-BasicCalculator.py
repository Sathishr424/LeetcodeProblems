# Last updated: 25/7/2025, 9:11:30 pm
class Solution:
    def calculate(self, calculate: str) -> int:
        n = len(calculate)

        def rec(index):
            # print('new', index)
            i = index
            left = 0
            op = ''
            while i < n:
                if calculate[i] == '(':
                    tmp = i
                    i, s = rec(i + 1)
                    # print('found pranthesis', (tmp, i), calculate[tmp:i+1], left, op, s)
                    if op == '-': left -= s
                    elif op == '+': left += s
                    else: left = s
                    op = ''
                elif calculate[i] == ')':
                    # print("return", (i, left))
                    return i, left
                elif calculate[i] == '+':
                    op = '+'
                elif calculate[i] == '-':
                    op = '-'
                elif calculate[i] != ' ':
                    curr = 0
                    j = i
                    while j < n and calculate[j] in '0123456789':
                        curr = curr * 10 + int(calculate[j])
                        j += 1
                    if op == '+': left += curr
                    elif op == '-': left -= curr
                    else: left = curr
                    op = ''
                    i = j - 1
                # print((i, calculate[index:i+1]), left, op)
                i += 1
            return left, i
        
        return rec(0)[0]