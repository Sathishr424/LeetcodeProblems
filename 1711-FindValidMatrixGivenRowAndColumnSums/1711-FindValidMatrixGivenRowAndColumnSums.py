# Last updated: 12/6/2025, 5:40:52 am
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        
        ret = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            if rowSum[i] == 0: continue
            for j in range(n):
                diff = min(rowSum[i], colSum[j])
                if diff > 0:
                    ret[i][j] = diff
                    rowSum[i] -= diff
                    colSum[j] -= diff
        
        return ret
        