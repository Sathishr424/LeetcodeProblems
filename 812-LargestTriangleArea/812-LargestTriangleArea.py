# Last updated: 27/9/2025, 1:42:56 pm
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)

        def getDis(a, b):
            return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

        max_area = 0
        for i in range(n):
            x = points[i]
            for j in range(i+1, n):
                y = points[j]
                for k in range(j+1, n):
                    z = points[k]


                    a = getDis(x, y)
                    b = getDis(x, z)
                    c = getDis(y, z)

                    s = (a + b + c) / 2
                    area = sqrt(abs(s * (s - a) * (s - b) * (s - c)))

                    max_area = max(max_area, area)
            
        return max_area
                    
