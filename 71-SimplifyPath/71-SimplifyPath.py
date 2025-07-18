# Last updated: 12/6/2025, 5:53:59 am
class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        stack = []
        curr = ''
        for char in path:
            if char == '/':
                if curr == '..':
                    if stack: stack.pop()
                elif curr and curr != '.': 
                    stack.append(curr)
                curr = ''
            else:
                curr += char
        
        if curr == '..':
            if stack: stack.pop()
        elif curr and curr != '.': 
            stack.append(curr)
        return '/' + '/'.join(stack)