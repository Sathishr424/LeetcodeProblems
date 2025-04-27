# Last updated: 27/4/2025, 4:50:56 pm
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        horizontal = [[] for _ in range(n+1)]
        vertical = [[] for _ in range(n+1)]

        for i, j in sorted(buildings):
            vertical[j].append(i)
        
        for i, j in sorted(buildings, key=lambda x: x[1]):
            horizontal[i].append(j)
        
        ret = 0
        for i, j in buildings:
            cnt = bisect_left(horizontal[i], j) != 0
            cnt += bisect_left(horizontal[i], j+1) != len(horizontal[i])
            cnt += bisect_left(vertical[j], i) != 0
            cnt += bisect_left(vertical[j], i+1) != len(vertical[j])

            if cnt == 4: ret += 1

        return ret
            