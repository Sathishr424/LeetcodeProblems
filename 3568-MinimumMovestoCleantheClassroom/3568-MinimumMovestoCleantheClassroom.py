# Last updated: 9/1/2026, 7:12:27 PM
1class Solution:
2    def minMoves(self, cr: List[str], energy: int) -> int:
3        m = len(cr)
4        n = len(cr[0])
5
6        pos = [0, 0]
7        litter = 0
8        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
9        grid = [[0] * n for _ in range(m)]
10
11        for i in range(m):
12            for j in range(n):
13                if cr[i][j] == 'S':
14                    pos = [i, j]
15                elif cr[i][j] == 'L':
16                    grid[i][j] = litter
17                    litter += 1
18        full_litter = (1 << litter) - 1
19
20        stack = deque([(pos[0], pos[1], 0, energy, 0)])
21        visited = {}
22
23        # print(format(full_litter, '010b'))
24        while stack:
25            i, j, litters, e, move = stack.popleft()
26            # print(i, j, format(litters, '010b'), e, move)
27            # if move > ret: break
28            if litters == full_litter:
29                return move
30                # ret = min(ret, move)
31                # continue
32            key = (i, j, litters)
33            if key in visited and visited[key] >= e: continue
34            if e == 0: continue
35            visited[key] = e
36        
37            for i2, j2 in DIR:
38                i2 += i
39                j2 += j
40            
41                if 0 <= i2 < m and 0 <= j2 < n and cr[i2][j2] != 'X':
42                    curr = cr[i2][j2]
43                    new_e = e - 1
44                    new_litters = litters
45                    if curr == 'L':
46                        new_litters |= 1 << grid[i2][j2]
47                    elif curr == 'R':
48                        new_e = energy
49                    
50                    stack.append((i2, j2, new_litters, new_e, move + 1))
51        
52        return -1