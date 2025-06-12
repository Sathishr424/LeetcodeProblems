# Last updated: 12/6/2025, 5:41:14 am
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        memo = {}
        memo["0,0"] = 1
        for d in path:
            if d == 'N': y -= 1
            elif d == 'S': y += 1
            elif d == 'W': x -= 1
            elif d == 'E': x += 1
            key = f"{x},{y}"
            if key in memo: return True
            memo[key] = 1
        return False