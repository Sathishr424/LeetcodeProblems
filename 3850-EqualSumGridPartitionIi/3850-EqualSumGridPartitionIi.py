# Last updated: 12/6/2025, 5:33:31 am
N = 10**5
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        total = 0

        exist_freq = [0] * (N + 1)
        exist_freq[0] += 1
        maxi = 0

        for i in range(m):
            for j in range(n):
                total += grid[i][j]
                exist_freq[grid[i][j]] += 1
        
        def check(grid, freq):
            exist = freq + []
            curr = 0
            for i in range(m-1):
                for j in range(n):
                    val = grid[i][j]
                    curr += val
                    exist[val] -= 1
                
                rem = total - curr
                need = rem - curr
                if need < 0 or need > N: continue

                if need == 0: return True
                elif n == 1:
                    if need == grid[i+1][0] or need == grid[m-1][0]: return True
                elif i == m-2:
                    if need == grid[i+1][0] or need == grid[i+1][n-1]:
                        return True
                elif exist[need]:
                    return True
            
            curr = 0
            exist = freq
            for j in range(n-1):
                for i in range(m):
                    val = grid[i][j]
                    curr += val
                    exist[val] -= 1
                
                rem = total - curr
                need = rem - curr
                if need < 0 or need > N: continue

                if need == 0: return True
                elif m == 1:
                    if need == grid[0][j+1] or need == grid[0][n-1]: return True
                elif j == n-2:
                    if need == grid[0][j+1] or need == grid[m-1][j+1]: 
                        return True
                elif exist[need]:
                    return True
            
            return False

        return check(grid, exist_freq + []) or check([row[::-1] for row in grid][::-1], exist_freq + [])