# Last updated: 27/9/2025, 1:48:55 pm
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)

        def getDis(a, b):
            return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

        max_area = 0
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                for k in range(j+1, n):
                    x3, y3 = points[k]


                    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

                    max_area = max(max_area, area)
            
        return max_area
                    
