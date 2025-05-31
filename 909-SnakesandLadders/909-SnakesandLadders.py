# Last updated: 31/5/2025, 3:10:49 pm
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        area = n * n

        grid = [0] * area
        pos = 0

        def addToGrid(i, j):
            if board[i][j] == -1:
                grid[pos] = pos
            else:
                grid[pos] = board[i][j] - 1

        for i in range(n-1, -1, -1):
            if (n-i) % 2 == 0:
                for j in range(n-1, -1, -1):
                    addToGrid(i, j)
                    pos += 1
            else: 
                for j in range(n):
                    addToGrid(i, j)
                    pos += 1
        
        stack = deque([(0, 0)])
        visited = [0] * area
        while stack:
            pos, moves = stack.popleft()

            if pos == area-1: return moves

            for roll in range(1, 7):
                new_pos = pos + roll
                if new_pos >= area: break
                if visited[new_pos]: continue
                visited[new_pos] = 1

                stack.append((grid[new_pos], moves + 1))
        
        return -1

                

