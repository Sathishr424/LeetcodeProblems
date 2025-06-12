# Last updated: 12/6/2025, 5:34:46 am
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for i in range(n):
            j = 0
            arr = []
            while i+j < n:
                arr.append(grid[i+j][j])
                j += 1
            arr.sort(reverse=True)
            j -= 1
            while j >= 0:
                grid[i+j][j] = arr.pop()
                j -= 1
        
        for i in range(1, n):
            j = 0
            arr = []
            while i+j < n:
                arr.append(grid[j][i+j])
                j += 1
            arr.sort()
            j -= 1
            while j >= 0:
                grid[j][i+j] = arr.pop()
                j -= 1
        
        return grid
                