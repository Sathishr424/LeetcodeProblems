# Last updated: 31/5/2025, 3:23:03 pm
cmin = lambda x, y: x if x < y else y
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        area = n * n

        stack = [0]
        pos = 0

        grid = []
        moves = 0

        def addToGrid(i, j):
            if board[i][j] == -1:
                grid.append(pos)
            else:
                grid.append(board[i][j] - 1)

        for i in range(n-1, -1, -1):
            if (n-i) % 2 == 0:
                for j in range(n-1, -1, -1):
                    addToGrid(i, j)
                    pos += 1
            else: 
                for j in range(n):
                    addToGrid(i, j)
                    pos += 1
        
        while stack:
            new_stack = []
            for pos in stack:
                for new_pos in range(pos+1, cmin(n*n, pos+7)):
                    if grid[new_pos] == -1: continue
                    
                    if grid[new_pos] == area-1: return moves + 1
                    new_stack.append(grid[new_pos])
                    grid[new_pos] = -1
            
            stack = new_stack
            moves += 1
        
        return -1