# Last updated: 4/5/2025, 9:42:45 am
class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        if N == 0: return [[0]]
        m = 2**N

        ret = [[0] * m for _ in range(m)]

        def processFill(i, j, rows, val):
            if rows == 1:
                ret[i][j] = val
                return ret[i][j]-1
            
            half = rows//2
            for k in range(0, rows, rows//2):
                val = processFill(i, j, half, val)
                i += half
            j += k
            i -= half
            for k in range(0, rows, rows//2):
                val = processFill(i, j, half, val)
                i -= half
            return val
                    
        processFill(0, 0, m, 2**(2*N) - 1)
        return ret
                

        