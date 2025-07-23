# Last updated: 23/7/2025, 11:43:51 am
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        n = len(s)
        a, b = 'ab', 'ba'
        if y > x:
            x, y = y, x
            a, b = b, a
        
        stack = []
        
        ret = 0
        for char in s:
            if stack:
                if stack[-1] + char == a:
                    stack.pop()
                    ret += x
                    continue
            stack.append(char)
        
        new_stack = []
        for char in stack:
            if new_stack:
                if new_stack[-1] + char == a:
                    new_stack.pop()
                    ret += x
                    continue
                if new_stack[-1] + char == b:
                    new_stack.pop()
                    ret += y
                    continue
            new_stack.append(char)
        
        return ret