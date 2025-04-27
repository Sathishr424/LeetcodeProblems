# Last updated: 27/4/2025, 4:57:11 pm
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        horizontal = [[float('inf'), -float('inf')] for _ in range(n+1)]
        vertical = [[float('inf'), -float('inf')] for _ in range(n+1)]

        for i, j in buildings:
            vertical[j][0] = min(vertical[j][0], i)
            vertical[j][1] = max(vertical[j][1], i)

            horizontal[i][0] = min(horizontal[i][0], j)
            horizontal[i][1] = max(horizontal[i][1], j)
        
        ret = 0
        for i, j in buildings:
            if j > horizontal[i][0] and j < horizontal[i][1] and i > vertical[j][0] and i < vertical[j][1]: ret += 1

        return ret
            