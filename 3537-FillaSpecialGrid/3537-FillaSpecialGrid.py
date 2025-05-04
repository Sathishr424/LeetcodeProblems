# Last updated: 4/5/2025, 9:47:01 am
class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        m = 1 << N
        ret = [[0] * m for _ in range(m)]

        def processFill(i, j, rows, val):
            if rows == 1:
                ret[i][j] = val
                return ret[i][j]-1
            
            half = rows//2
            for _ in range(2):
                val = processFill(i, j, half, val)
                i += half
            j += half
            i -= half
            for _ in range(2):
                val = processFill(i, j, half, val)
                i -= half
            return val
        
        processFill(0, 0, m, (1 << (2*N)) - 1)
        return ret
                

        