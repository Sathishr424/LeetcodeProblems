# Last updated: 9/5/2025, 2:17:35 am
class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        seen = {}

        for i in range(m):
            mask = 0
            for j in range(n):
                mask += grid[i][j] << (n - j - 1)

            # If the bitmask is zero, we immediately have a valid subset
            if mask == 0: 
                return [i]

            for prev_mask, prev_index in seen.items():
                if prev_mask & mask == 0:
                    return [prev_index, i]

            seen[mask] = i
        
        return []
        