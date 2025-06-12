# Last updated: 12/6/2025, 5:50:51 am
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        row = []
        left = 0
        for j in range(n):
            neighbors = 0
            if j+1 < n:
                neighbors += board[0][j+1]
            if j-1 > -1:
                neighbors += left
            if m > 1:
                neighbors += board[0+1][j]
                if j+1 < n: neighbors += board[0+1][j+1]
                if j-1 > -1: neighbors += board[0+1][j-1]
            left = board[0][j]
            row.append(board[0][j])
            if board[0][j]:
                if neighbors < 2 or neighbors > 3:
                    board[0][j] = 0
            else:
                if neighbors == 3:
                    board[0][j] = 1
        
        for i in range(1, m):
            new_row = []
            left = 0
            for j in range(n):
                neighbors = 0
                neighbors += row[j]
                if j+1 < n:
                    neighbors += row[j+1]
                    neighbors += board[i][j+1]
                if j-1 > -1:
                    neighbors += row[j-1]
                    neighbors += left
                if i+1 < m:
                    neighbors += board[i+1][j]
                    if j+1 < n: neighbors += board[i+1][j+1]
                    if j-1 > -1: neighbors += board[i+1][j-1]
                left = board[i][j]
                new_row.append(board[i][j])
                if board[i][j]:
                    if neighbors < 2 or neighbors > 3:
                        board[i][j] = 0
                else:
                    if neighbors == 3:
                        board[i][j] = 1
            row = new_row
        