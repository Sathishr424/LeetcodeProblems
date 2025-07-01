# Last updated: 1/7/2025, 8:10:11 pm
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])
        pos = [0, 0]
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        keys = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    pos = [i, j]
                elif 97 <= ord(grid[i][j]) <= 122:
                    keys += 1
        
        unlocked = (1 << keys) - 1
        stack = deque([(pos[0], pos[1], 0, 0)])

        visited = [[[0] * (1 << keys) for _ in range(n)] for _ in range(m)]
        while stack:
            i, j, k, move = stack.popleft()

            if k == unlocked: return move
            if visited[i][j][k]: continue
            visited[i][j][k] = 1

            for i2, j2 in DIR:
                i2 += i
                j2 += j

                if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] != '#':
                    new_k = k
                    
                    if 97 <= ord(grid[i2][j2]) <= 122:
                        new_k |= 1 << (ord(grid[i2][j2]) - 97)
                    elif 65 <= ord(grid[i2][j2]) <= 90:
                        if new_k & (1 << (ord(grid[i2][j2]) - 65)) == 0: continue
                    
                    stack.append((i2, j2, new_k, move + 1))
        
        return -1