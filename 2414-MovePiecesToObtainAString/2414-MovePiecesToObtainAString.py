# Last updated: 12/6/2025, 5:38:13 am
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(target)

        stack = deque([])
        dash = 0
        for i in range(n):
            if start[i] != '_':
                stack.append(i)
            else:
                dash += 1
        
        for i in range(n):
            if target[i] == 'L':
                if len(stack) == 0: return False
                s = stack.popleft()
                if s < i or start[s] != target[i]: return False
            elif target[i] == 'R':
                if len(stack) == 0: return False
                s = stack.popleft()
                if s > i or start[s] != target[i]: return False
            else:
                dash -= 1
                
        return dash == 0
            

