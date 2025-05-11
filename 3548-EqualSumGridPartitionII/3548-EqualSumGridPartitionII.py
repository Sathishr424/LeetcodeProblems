# Last updated: 11/5/2025, 12:04:24 pm
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        total = 0

        for i in range(m):
            for j in range(n):
                total += grid[i][j]
        
        def check(grid):
            exist = defaultdict(int)
            exist_col = defaultdict(int)
            exist[0] += 1
            exist_col[0] += 1
            for i in range(m):
                for j in range(n):
                    exist[grid[i][j]] += 1
                    exist_col[grid[i][j]] += 1
        
            curr = 0
            for i in range(m-1):
                for j in range(n):
                    val = grid[i][j]
                    curr += val
                    exist[val] -= 1
                
                rem = total - curr
                need = rem - curr
                if need == 0: return True
                elif n == 1:
                    if need == grid[i+1][0] or need == grid[m-1][0]: return True
                elif i == m-2:
                    if need == grid[i+1][0] or need == grid[i+1][n-1]:
                        # print("ROW_last", (i, m), curr, (rem, need))
                        return True
                elif exist[need]:
                    # print("ROW", (i, m), curr, (rem, need))
                    return True
            
            curr = 0
            for j in range(n-1):
                for i in range(m):
                    val = grid[i][j]
                    curr += val
                    exist_col[val] -= 1
                
                rem = total - curr
                need = rem - curr
                if need == 0: return True
                elif m == 1:
                    if need == grid[0][j+1] or need == grid[0][n-1]: return True
                elif j == n-2:
                    if need == grid[0][j+1] or need == grid[m-1][j+1]: 
                        # print("COLUMN_last", (j, n), curr, (rem, need))
                        return True
                elif exist_col[need]:
                    # print("COLUMN", (j, n), curr, (rem, need))
                    return True
            
            return False

        return check(grid) or check([row[::-1] for row in grid][::-1])