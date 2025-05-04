# Last updated: 4/5/2025, 9:34:52 am
class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        if N == 0: return [[0]]
        m = 2**N

        ret = [[0] * m for _ in range(m)]

        def fill(rowStart, rows, colStart, cols, val):
            j = 0
            while j < cols:
                if j % 2 == 0:
                    i = 0
                    while i < rows:
                        ret[rowStart+i][colStart+j] = val
                        val -= 1
                        i += 1
                else:
                    i = rows-1
                    while i >= 0:
                        ret[rowStart+i][colStart+j] = val
                        val -= 1
                        i -= 1
                j += 1
            return val

        def processFill(i, j, rows, val):
            if rows == 2:
                return fill(i, rows, j, rows, val)
            else:
                tmp = i
                half = rows//2
                for k in range(0, rows, rows//2):
                    val = processFill(i, j, half, val)
                    i += half
                j += k
                i = i-half
                for k in range(0, rows, rows//2):
                    val = processFill(i, j, half, val)
                    i -= half
                return val
                    
        processFill(0, 0, m, 2**(2*N) - 1)
        return ret
                

        