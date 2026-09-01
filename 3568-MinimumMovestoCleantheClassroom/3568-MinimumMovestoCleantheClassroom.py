# Last updated: 9/1/2026, 7:22:11 PM
1class Solution:
2    def minMoves(self, classroom: List[str], energy: int) -> int:
3        m = len(classroom)
4        n = len(classroom[0])
5
6        index = 0
7        litters = [[-1] * n for _ in range(m)]
8        l_index = 0
9        for i in range(m):
10            for j in range(n):
11                if classroom[i][j] == 'S':
12                    index = i * n + j
13                elif classroom[i][j] == 'L':
14                    litters[i][j] = l_index
15                    l_index += 1
16
17        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
18        full_mask = (1 << l_index) - 1
19
20        stack = [(0, index // n, index % n, energy, 0)]
21        dis = [[[-1 for _ in range(full_mask + 1)] for _ in range(n)] for _ in range(m)]
22
23        while stack:
24            new_stack = []
25            for moves, i, j, rem, mask in stack:
26                if mask == full_mask: return moves
27                if rem == 0: continue
28
29                for i2, j2 in DIR:
30                    i2 += i
31                    j2 += j
32
33                    if 0 <= i2 < m and 0 <= j2 < n and classroom[i2][j2] != 'X':
34                        new_rem = rem - 1
35                        new_mask = mask
36                        if classroom[i2][j2] == 'R':
37                            new_rem = energy
38                        elif classroom[i2][j2] == 'L':
39                            new_mask |= (1 << litters[i2][j2])
40
41                        if dis[i2][j2][new_mask] < new_rem:
42                            dis[i2][j2][new_mask] = new_rem
43                            new_stack.append((moves + 1, i2, j2, new_rem, new_mask))
44            stack = new_stack
45
46        return -1