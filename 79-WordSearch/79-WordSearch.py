# Last updated: 12/6/2025, 5:53:47 am
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def is_valid(i, j):
            return not (i == -1 or i == m or j == -1 or j == n)
        def dfs(i, j, index):
            if index == len(word): return True
            tmp = board[i][j]
            board[i][j] = '-'
            if is_valid(i-1, j) and board[i-1][j] == word[index] and dfs(i-1, j, index+1): return True
            if is_valid(i+1, j) and board[i+1][j] == word[index] and dfs(i+1, j, index+1): return True
            if is_valid(i, j-1) and board[i][j-1] == word[index] and dfs(i, j-1, index+1): return True
            if is_valid(i, j+1) and board[i][j+1] == word[index] and dfs(i, j+1, index+1): return True
            board[i][j] = tmp
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 1): return True
        
        return False
