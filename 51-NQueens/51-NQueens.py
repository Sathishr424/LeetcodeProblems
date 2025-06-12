# Last updated: 12/6/2025, 5:54:26 am
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        tmp = [['.' for _ in range(n)] for _ in range(n)]
        def rec(row, pd, nd, cols, ans):
            for i in range(n):
                if i in cols: continue
                if row-i in pd: continue
                if row+i in nd: continue

                if row == n-1:
                    ans[row][i] = 'Q'
                    res.append([''.join(a) for a in ans])
                    ans[row][i] = '.'
                else:
                    ans[row][i] = 'Q'
                    nd[row+i] = 1
                    pd[row-i] = 1
                    cols[i] = 1
                    rec(row+1, pd, nd, cols, ans)
                    ans[row][i] = '.'
                    del nd[row+i]
                    del pd[row-i]
                    del cols[i]
        rec(0, {}, {}, {}, tmp)
        return res
        