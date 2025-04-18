# Last updated: 19/4/2025, 2:45:47 am
class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        sorted_pos_and_speed = []
        for i in range(len(pos)):
            sorted_pos_and_speed.append((pos[i], speed[i]))
        sorted_pos_and_speed.sort()

        stack = []

        for p, s in sorted_pos_and_speed:
            d = (target-p) / s
            while stack and stack[-1] <= d:
                stack.pop()
            stack.append(d)
        
        return len(stack)