# Last updated: 12/6/2025, 5:52:57 am
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]
        for i in range(1, numRows):
            ret.append([1] * (i+1))
            for j in range(1,i):
                ret[i][j] = ret[i-1][j] + ret[i-1][j-1]
        return ret