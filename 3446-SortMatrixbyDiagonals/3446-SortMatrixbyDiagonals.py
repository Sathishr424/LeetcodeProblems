# Last updated: 28/8/2025, 11:00:56 am
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for index in range(n):
            i = index
            j = 0
            nums = []
            while i < n and j < n:
                nums.append(grid[i][j])
                i += 1
                j += 1
            nums.sort()
            i = index
            j = 0
            while i < n and j < n:
                grid[i][j] = nums.pop()
                i += 1
                j += 1
        
        for index in range(1, n):
            i = 0
            j = index
            nums = []
            while i < n and j < n:
                nums.append(grid[i][j])
                i += 1
                j += 1
            nums.sort(reverse=True)
            i = 0
            j = index
            while i < n and j < n:
                grid[i][j] = nums.pop()
                i += 1
                j += 1

        return grid