# Last updated: 12/6/2025, 5:44:08 am
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        ret = []
        for i in range(rows):
            for j in range(cols):
                ret.append([i, j])
        
        ret.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))

        return ret