# Last updated: 23/8/2025, 4:28:28 pm
cmin = lambda x, y: x if x < y else y
cmax = lambda x, y: x if x > y else y

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        @cache
        def split(t, r, b, l):
            min_area = inf
            ones = 0
            for i in range(t, b + 1):
                for j in range(l, r + 1):
                    if grid[i][j] == 1:
                        ones += 1
            
            rem_ones = ones
            for i in range(t, b + 1):
                for j in range(l, r + 1):
                    if grid[i][j] == 1:
                        rem_ones -= 1
                if rem_ones and rem_ones < ones:
                    min_area = cmin(min_area, getArea(t, r, i, l) + getArea(i+1, r, b, l))
            
            rem_ones = ones
            for j in range(l, r + 1):
                for i in range(t, b + 1):
                    if grid[i][j] == 1:
                        rem_ones -= 1
                if rem_ones and rem_ones < ones:
                    min_area = cmin(min_area, getArea(t, j, b, l) + getArea(t, r, b, j+1))

            return min_area

        @cache
        def getArea(t, r, b, l):
            left = inf
            top = inf
            right = 0
            bottom = 0

            for i in range(t, b + 1):
                for j in range(l, r + 1):
                    if grid[i][j] == 1:
                        top = cmin(top, i)
                        right = cmax(right, j)
                        bottom = cmax(bottom, i)
                        left = cmin(left, j)
            return (right - left + 1) * (bottom - top + 1)

        def getAns():
            ones = 0
            ans = inf
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        ones += 1
            
            rem_ones = ones
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        rem_ones -= 1
                if rem_ones and rem_ones < ones:
                    ans = cmin(ans, split(0, n-1, i, 0) + getArea(i+1, n-1, m-1, 0))
                    ans = cmin(ans, getArea(0, n-1, i, 0) + split(i+1, n-1, m-1, 0))
            
            rem_ones = ones
            for j in range(n):
                for i in range(m):
                    if grid[i][j] == 1:
                        rem_ones -= 1
                if rem_ones and rem_ones < ones:
                    ans = cmin(ans, split(0, j, m-1, 0) + getArea(0, n-1, m-1, j+1))
                    ans = cmin(ans, getArea(0, j, m-1, 0) + split(0, n-1, m-1, j+1))
                    
            return ans

        return getAns()
        