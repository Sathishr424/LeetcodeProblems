# Last updated: 3/9/2025, 4:25:39 pm
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)

        row = 0
        col = 0
        for x, y in points:
            row = max(row, y)
            col = max(col, x)
        row += 1
        col += 1
        points.sort(key=lambda x: (x[0], -x[1]))

        points_on_grid = [[0] * col for _ in range(row)]
        for x, y in points:
            points_on_grid[y][x] = 1
        
        prefix = [[0] * (col + 1) for _ in range(row + 1)]
        for i in range(1, row + 1):
            s = 0
            for j in range(1, col + 1):
                s += points_on_grid[i-1][j-1]
                prefix[i][j] = s + prefix[i - 1][j]

        count = 0
        for i in range(n):
            x, y = points[i] # lower right
            for j in range(i):
                x2, y2 = points[j] # Upper left

                if y2 < y: continue
                
                full = prefix[y2 + 1][x + 1]
                bottom_left = prefix[y2 + 1][x2]
                top_right = prefix[y][x + 1]
                center = prefix[y][x2]
                
                if full - (bottom_left + top_right - center) == 2:
                    count += 1
            
        return count