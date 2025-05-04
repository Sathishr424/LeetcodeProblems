# Last updated: 4/5/2025, 9:50:20 am
class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        m = 1 << N
        ret = [[0] * m for _ in range(m)]

        def processFill(i, j, rows, val):
            if rows == 1:
                ret[i][j] = val
                return ret[i][j]-1
            
            half = rows//2

            val = processFill(i, j, half, val)
            val = processFill(i+half, j, half, val)
            val = processFill(i+half, j+half, half, val)

            return processFill(i, j+half, half, val)
        
        processFill(0, 0, m, (1 << (2*N)) - 1)
        return ret