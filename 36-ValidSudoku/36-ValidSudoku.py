# Last updated: 21/7/2025, 3:17:24 pm
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                box = (i // 3) * 3 + (j // 3)
                pos = 1 << (int(board[i][j]) - 1)
                if rows[i] & pos != 0 or cols[j] & pos != 0 or boxes[box] & pos != 0: return False
                rows[i] |= pos
                cols[j] |= pos
                boxes[box] |= pos
        
        return True