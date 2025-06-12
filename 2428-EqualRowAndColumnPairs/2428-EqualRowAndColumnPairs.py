# Last updated: 12/6/2025, 5:38:09 am
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ret = 0

        rows = ['' for _ in range(n)]
        cols = ['' for _ in range(n)]

        for row in range(n):
            for col in range(n):
                rows[col] = rows[col]  + ',' + str(grid[row][col])
                cols[row] = cols[row]  + ',' + str(grid[row][col])

        hash = {}
        for row in rows:
            if row in hash:
                hash[row] += 1
            else:
                hash[row] = 1
        
        ret = 0

        for col in cols:
            if col in hash:
                ret += hash[col]
        
        # print(rows)
        # print(cols)
        
        return ret