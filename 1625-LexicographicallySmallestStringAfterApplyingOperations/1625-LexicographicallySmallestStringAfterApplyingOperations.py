# Last updated: 19/10/2025, 9:51:06 pm
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)

        stack = deque([s])
        best = s
        visited = {}

        while stack:
            new_s = stack.pop()
            if new_s in visited: continue
            
            left = new_s[:n-b]
            right = new_s[n-b:]
            stack.append(right + left)

            visited[new_s] = 1
            best = min(best, new_s)

            stack.append(''.join([str((int(num) + a) % 10) if i % 2 else num for i, num in enumerate(new_s)]))
    
        return best
