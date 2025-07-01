# Last updated: 1/7/2025, 7:57:01 pm
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])
        pos = [0, 0]
        keys = {}
        locks = {}
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    pos = [i, j]
                elif 97 <= ord(grid[i][j]) <= 122:
                    keys[(i, j)] = ord(grid[i][j]) - 97
                elif 65 <= ord(grid[i][j]) <= 90:
                    locks[(i, j)] = ord(grid[i][j]) - 65
        unlocked = (1 << len(locks)) - 1
        stack = deque([(pos[0], pos[1], 0, 0)])

        visited = {}
        while stack:
            i, j, k, move = stack.popleft()

            if k == unlocked: return move
            key = (i, j, k)
            if key in visited: continue
            visited[key] = 1

            for i2, j2 in DIR:
                i2 += i
                j2 += j

                if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] != '#':
                    curr = (i2, j2)
                    new_k = k
                    if curr in keys:
                        new_k |= 1 << keys[curr]
                    elif curr in locks and new_k & (1 << locks[curr]) == 0:
                        continue
                    
                    stack.append((i2, j2, new_k, move + 1))
        
        return -1