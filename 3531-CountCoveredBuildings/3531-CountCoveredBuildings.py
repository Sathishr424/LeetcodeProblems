# Last updated: 27/4/2025, 5:14:20 pm
cmin = lambda x, y: x if x < y else y
cmax = lambda x, y: x if x > y else y

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        horizontal_min = [float('inf') for _ in range(n+1)]
        horizontal_max = [-float('inf') for _ in range(n+1)]
        vertical_min = [float('inf') for _ in range(n+1)]
        vertical_max = [-float('inf') for _ in range(n+1)]

        for i, j in buildings:
            vertical_min[j] = cmin(vertical_min[j], i)
            vertical_max[j] = cmax(vertical_max[j], i)

            horizontal_min[i] = cmin(horizontal_min[i], j)
            horizontal_max[i] = cmax(horizontal_max[i], j)
        
        ret = 0
        for i, j in buildings:
            if j > horizontal_min[i] and j < horizontal_max[i] and i > vertical_min[j] and i < vertical_max[j]: ret += 1

        return ret
            