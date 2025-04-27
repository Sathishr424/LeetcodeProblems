# Last updated: 27/4/2025, 5:11:55 pm
cmin = lambda x, y: x if x < y else y
cmax = lambda x, y: x if x > y else y

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        horizontal = [[float('inf'), -float('inf')] for _ in range(n+1)]
        vertical = [[float('inf'), -float('inf')] for _ in range(n+1)]

        for i, j in buildings:
            vertical[j][0] = cmin(vertical[j][0], i)
            vertical[j][1] = cmax(vertical[j][1], i)

            horizontal[i][0] = cmin(horizontal[i][0], j)
            horizontal[i][1] = cmax(horizontal[i][1], j)
        
        ret = 0
        for i, j in buildings:
            if j > horizontal[i][0] and j < horizontal[i][1] and i > vertical[j][0] and i < vertical[j][1]: ret += 1

        return ret
            