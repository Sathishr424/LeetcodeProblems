# Last updated: 30/8/2025, 10:29:38 am
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for row in range(n):
            for col in range(n):
                if board[row][col] == '.': continue
                box = (row // 3) * 3 + (col // 3)
                cell = int(board[row][col]) - 1
                mask = 1 << cell
                if rows[row] & mask != 0:
                    return False
                if cols[col] & mask != 0:
                    return False
                if boxes[box] & mask != 0:
                    return False
                
                rows[row] |= mask
                cols[col] |= mask
                boxes[box] |= mask
        
        return True