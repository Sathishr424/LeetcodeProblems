# Last updated: 12/6/2025, 5:54:41 am
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.': continue
                elif val in rows[i]:  return False
                elif val in cols[j]: return False
                z = ((i//3)*3)+(j//3)
                if val in boxes[z]: return False
                rows[i][val] = 1
                cols[j][val] = 1
                boxes[z][val] = 1
        return True

