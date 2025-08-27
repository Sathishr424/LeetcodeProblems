# Last updated: 27/8/2025, 1:14:36 pm
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        DIR = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        can_rotate = [1, 2, 3, 0]

        def checkRotate(i, j, d, need, rotated):
            i2 = i + DIR[d][0]
            j2 = j + DIR[d][1]

            if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == need:
                return rec(i2, j2, d, rotated) + 1
            return 0

        @cache
        def rec(i, j, d, rotated):
            # print(i, j, d, rotated)
            ans = 0
            if grid[i][j] == 2:
                ans = max(ans, checkRotate(i, j, d, 0, rotated))
                
                if not rotated:
                    ans = max(ans, checkRotate(i, j, can_rotate[d], 0, True))
            else:
                ans = max(ans, checkRotate(i, j, d, 2, rotated))
                
                if not rotated:
                    ans = max(ans, checkRotate(i, j, can_rotate[d], 2, True))

            return ans
        
        longest = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for d in range(4):
                        longest = max(longest, checkRotate(i, j, d, 2, False) + 1)
        
        return longest