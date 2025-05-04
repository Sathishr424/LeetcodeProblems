# Last updated: 4/5/2025, 9:53:45 am
class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        m = 1 << N
        ret = [[0] * m for _ in range(m)]

        def fill(i, j, n, val):
            if n == 1:
                ret[i][j] = val
                return val-1
            
            half = n//2

            val = fill(i, j, half, val)
            val = fill(i+half, j, half, val)
            val = fill(i+half, j+half, half, val)

            return fill(i, j+half, half, val)
        
        fill(0, 0, m, (1 << (2*N)) - 1)
        return ret