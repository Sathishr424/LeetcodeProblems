# Last updated: 31/5/2025, 3:25:15 pm
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
                for roll in range(1, 7):
                    new_pos = pos + roll
                    if new_pos >= area: break
                    if visited[new_pos]: continue
                    if grid[new_pos] == area-1: return moves + 1
                    visited[new_pos] = 1

                    new_stack.append(grid[new_pos])
            stack = new_stack
            moves += 1
        
        return -1

                

