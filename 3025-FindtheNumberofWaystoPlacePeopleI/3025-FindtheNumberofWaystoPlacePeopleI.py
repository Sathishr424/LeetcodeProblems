# Last updated: 2/9/2025, 11:39:12 am
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)

        points.sort(key=lambda x: (x[0], -x[1]))
        max_x = 0
        max_y = 0
        for x, y in points:
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        max_x += 1
        max_y += 1

        points_on_grid = [[0] * max_x for _ in range(max_y)]
        for x, y in points:
            points_on_grid[y][x] = 1
        
        prefix = [[] for _ in range(max_y)]

        for i in range(max_y):
            prefix[i].append(0)
            s = 0
            for j in range(max_x):
                if points_on_grid[i][j] == 1:
                    s += 1
                prefix[i].append(s)

        def isValid(y, y2, x, x2):
            if y2 < y: return False
            for k in range(y + 1, y2):
                if prefix[k][x + 1] - prefix[k][x2] > 0: return False
            
            if y == y2:
                return prefix[y][x + 1] - prefix[y][x2] == 2
            return prefix[y][x + 1] - prefix[y][x2] == 1 and prefix[y2][x + 1] - prefix[y2][x2] == 1

        count = 0
        for i in range(n):
            x, y = points[i]
            for j in range(i):
                x2, y2 = points[j]
                ans = isValid(y, y2, x, x2)
                if ans:
                    count += 1
        
        return count