# Last updated: 12/25/2025, 7:11:20 PM
class Solution:
    def minMoves(self, cr: List[str], energy: int) -> int:
        m = len(cr)
        n = len(cr[0])

        pos = [0, 0]
        litter = 0
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        grid = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if cr[i][j] == 'S':
                    pos = [i, j]
                elif cr[i][j] == 'L':
                    grid[i][j] = litter
                    litter += 1
        full_litter = (1 << litter) - 1

        stack = deque([(pos[0], pos[1], 0, energy, 0)])
        visited = {}

        # print(format(full_litter, '010b'))
        while stack:
            i, j, litters, e, move = stack.popleft()
            # print(i, j, format(litters, '010b'), e, move)
            # if move > ret: break
            if litters == full_litter:
                return move
                # ret = min(ret, move)
                # continue
            key = (i, j, litters)
            if key in visited and visited[key] >= e: continue
            if e == 0: continue
            visited[key] = e
        
            for i2, j2 in DIR:
                i2 += i
                j2 += j
            
                if 0 <= i2 < m and 0 <= j2 < n and cr[i2][j2] != 'X':
                    curr = cr[i2][j2]
                    new_e = e - 1
                    new_litters = litters
                    if curr == 'L':
                        new_litters |= 1 << grid[i2][j2]
                    elif curr == 'R':
                        new_e = energy
                    
                    stack.append((i2, j2, new_litters, new_e, move + 1))
        
        return -1