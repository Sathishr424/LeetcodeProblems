# Last updated: 12/6/2025, 5:45:25 am
cmin = lambda x, y: x if x < y else y
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        area = n * n

        grid = []
        pos = 0

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
        
        stack = [0]
        moves = 0
        visited = [0] * area
        while stack:
            new_stack = []
            for pos in stack:
                for new_pos in range(pos+1, cmin(n*n, pos+7)):
                    if visited[new_pos]: continue
                    if grid[new_pos] == area-1: return moves + 1
                    
                    visited[new_pos] = 1
                    new_stack.append(grid[new_pos])
            stack = new_stack
            moves += 1
        
        return -1

                

