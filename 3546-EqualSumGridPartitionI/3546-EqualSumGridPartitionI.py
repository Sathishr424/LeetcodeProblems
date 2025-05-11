# Last updated: 11/5/2025, 10:21:52 am
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        total = 0
        
        for i in range(m):
            for j in range(n):
                total += grid[i][j]
        
        if total % 2: return False
        half = total // 2
            
        curr = 0
        for i in range(m):
            for j in range(n):
                curr += grid[i][j]

            if curr == half: return True    
        
        curr = 0
        for j in range(n):
            for i in range(m):
                curr += grid[i][j]

            if curr == half: return True

        return False
        