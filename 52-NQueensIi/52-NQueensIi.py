# Last updated: 12/6/2025, 5:54:25 am
class Solution:
    def totalNQueens(self, n: int) -> int:
        ret = 0
        def rec(row, pd, nd, cols):
            nonlocal ret
            for i in range(n):
                if i in cols: continue
                if row-i in pd: continue
                if row+i in nd: continue

                if row == n-1:
                    ret += 1
                else:
                    nd[row+i] = 1
                    pd[row-i] = 1
                    cols[i] = 1
                    rec(row+1, pd, nd, cols)
                    del nd[row+i]
                    del pd[row-i]
                    del cols[i]
        rec(0, {}, {}, {})
        return ret
        