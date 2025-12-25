# Last updated: 12/25/2025, 7:09:39 PM
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid)

        for i in range(k // 2):
            curr = grid[x + i][y:y+k]
            grid[x + i][y:y+k] = grid[x+(k-i-1)][y:y+k]
            grid[x+(k-i-1)][y:y+k] = curr

        return grid