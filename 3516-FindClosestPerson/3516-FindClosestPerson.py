# Last updated: 13/4/2025, 9:45:20 am
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a = abs(z-x)
        b = abs(y-z)

        if a > b: return 2
        elif a < b: return 1
        return 0
        