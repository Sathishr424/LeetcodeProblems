# Last updated: 12/6/2025, 5:52:37 am
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        if m == 1 or n == 1: return None
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]

        def dfs(i, j):
            board[i][j] = 'S'

            for x, y in dirs:
                i2 = i+x
                j2 = j+y

                if 0 <= i2 < m and 0 <= j2 < n and board[i2][j2] == 'O':
                    dfs(i2, j2)
        
        for i in range(0, m, m-1):
            for j in range(n):
                if board[i][j] == 'O':
                    dfs(i, j)
    
        for i in range(1, m-1):
            for j in range(0, n, n-1):
                if board[i][j] == 'O':
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'

                    

 