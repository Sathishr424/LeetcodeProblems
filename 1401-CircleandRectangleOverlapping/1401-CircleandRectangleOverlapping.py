# Last updated: 9/19/2026, 8:56:41 PM
1class Solution:
2    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
3        cx = max(x1, min(xCenter, x2))
4        cy = max(y1, min(yCenter, y2))
5
6        dx = xCenter - cx
7        dy = yCenter - cy
8
9        return dx * dx + dy * dy <= radius * radius