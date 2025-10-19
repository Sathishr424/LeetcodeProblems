# Last updated: 19/10/2025, 9:46:19 pm
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)

        stack = deque([s])
        best = s
        visited = {}

        while stack:
            new_s = stack.pop()
            # print(new_s)
            if new_s in visited: continue
            
            left = new_s[:n-b]
            right = new_s[n-b:]
            stack.append(right + left)

            visited[new_s] = 1
            best = min(best, new_s)

            curr = [int(d) for d in new_s]
            seen = {}
            num = curr[1]
            while num not in seen:
                seen[num] = 1
                num = (num + a) % 10

                for i in range(1, n, 2):
                    curr[i] = (curr[i] + a) % 10
                
                stack.append(''.join([str(num) for num in curr]))
        
        return best
