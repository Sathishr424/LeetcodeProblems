# Last updated: 12/6/2025, 5:36:48 am
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)

        robots = []

        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])
        
        robots.sort(key=lambda x: x[0])
        stack = []

        i = 0
        while i < n:
            curr = robots[i]
            while stack and stack[-1][2] != curr[2] and curr[2] == 'L':
                if curr[1] > stack[-1][1]:
                    stack.pop()
                    curr[1] -= 1
                elif curr[1] < stack[-1][1]:
                    stack[-1][1] -= 1
                    curr = None
                    break
                else:
                    stack.pop()
                    curr = None
                    break
            if curr: stack.append(curr)
            i += 1
        
        stack.sort(key=lambda x: x[-1])
        return [s[1] for s in stack]