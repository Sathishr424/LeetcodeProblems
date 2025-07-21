# Last updated: 21/7/2025, 3:00:30 pm
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        boxes = [0] * 9
        rows = [0] * 9
        cols = [0] * 9
        need = []
        n = 9
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.': need.append((i, j))
                else:
                    pos = 1 << (int(board[i][j]) - 1)
                    box = (i // 3) * 3 + (j // 3)
                    rows[i] |= pos
                    cols[j] |= pos
                    boxes[box] |= pos
        
        def dfs(index):
            if index == len(need):
                return True
            i, j = need[index]
            box = (i // 3) * 3 + (j // 3)
            for val in range(9):
                pos = 1 << val
                if rows[i] & pos == 0 and cols[j] & pos == 0 and boxes[box] & pos == 0:
                    r = rows[i]
                    c = cols[j]
                    b = boxes[box]
                    rows[i] |= pos
                    cols[j] |= pos
                    boxes[box] |= pos
                    board[i][j] = str(val + 1)
                    if dfs(index + 1): return True
                    rows[i] = r
                    cols[j] = c
                    boxes[box] = b
                    board[i][j] = '.'
            return False
        dfs(0)