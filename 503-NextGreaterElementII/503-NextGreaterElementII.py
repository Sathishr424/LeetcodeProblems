# Last updated: 19/4/2025, 2:43:49 am
class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(pos)):
            arr.append((pos[i], speed[i]))
        arr.sort()

        stack = []

        for p, s in arr:
            d = (target-p) / s
            while stack and stack[-1] <= d:
                stack.pop()
            stack.append(d)
        
        return len(stack)