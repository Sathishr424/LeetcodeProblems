# Last updated: 19/4/2025, 2:43:01 am
class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        n = len(pos)

        arr = []

        for i in range(n):
            arr.append((pos[i], speed[i]))
        
        arr.sort()

        ret = 0
        dis = 0
        stack = []

        for p, s in arr:
            d = (target-p) / s
            stack.append(d)
        # print(stack)
        arr = []
        for d in stack:
            while arr and arr[-1] <= d:
                arr.pop()
            arr.append(d)
        
        return len(arr)