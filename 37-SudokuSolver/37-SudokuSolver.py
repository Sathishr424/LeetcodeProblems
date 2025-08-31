# Last updated: 31/8/2025, 5:29:33 pm
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 9
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        emptyCells = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    emptyCells.append((i, j))
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.': continue
                cell = 1 << (int(board[i][j]) - 1)
                box = (i // 3) * 3 + (j // 3)
                rows[i] |= cell
                cols[j] |= cell
                boxes[box] |= cell
            
        # print([format(rows[i], '09b') for i in range(n)])
        # print([format(cols[i], '09b') for i in range(n)])
        # print([format(boxes[i], '09b') for i in range(n)])

        # print(emptyCells)
        ret = []
        def rec(index):
            if index == len(emptyCells):
                ret = [board[k][:] for k in range(n)]
                return True
            i, j = emptyCells[index]
            box = (i // 3) * 3 + (j // 3)
            for num in range(9):
                cell = 1 << num
                if rows[i] & cell == 0 and cols[j] & cell == 0 and boxes[box] & cell == 0:
                    board[i][j] = str(num + 1)
                    prev_row = rows[i]
                    prev_col = cols[j]
                    prev_box = boxes[box]
                    rows[i] |= cell
                    cols[j] |= cell
                    boxes[box] |= cell
                    if rec(index + 1): return True
                    rows[i] = prev_row
                    cols[j] = prev_col
                    boxes[box] = prev_box
            
            return False
        
        rec(0)
        return ret