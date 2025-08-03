# Last updated: 3/8/2025, 6:21:21 pm
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        elif numRows == 2: return [[1], [1, 1]]
        ret = [[1],[1,1]]

        for i in range(2, numRows):
            row = []
            row.append(1)
            for j in range(1, i):
                row.append(ret[len(ret) - 1][j - 1] + ret[len(ret) - 1][j])
            row.append(1)
            ret.append(row)
        
        return ret