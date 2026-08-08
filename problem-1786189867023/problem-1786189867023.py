# Last updated: 8/8/2026, 5:21:07 PM
1class Solution:
2    def createGrid(self, m: int, n: int, k: int) -> list[str]:
3        dir = [(1, 0), (0, 1)]
4        x = m * n
5        grid = [['.'] * n for _ in range(m)]
6        for i in range(m-1):
7            for j in range(1, n):
8                grid[i][j] = '#'
9
10        g_mask = 0
11        @cache
12        def rec(i, j):
13            if i == m-1 and j == n-1:
14                return 1
15            
16            ans = 0
17            for i2, j2 in dir:
18                i2 += i
19                j2 += j
20
21                if 0 <= i2 < m and 0 <= j2 < n and g_mask & (1 << (i2 * n + j2)) > 0:
22                    ans += rec(i2, j2)
23
24            return ans
25
26        def generateGrid(mask):
27            grid = [['#'] * n for _ in range(m)]
28                
29            for i in range(m):
30                for j in range(n):
31                    if mask & (1 << (i * n + j)):
32                        grid[i][j] = '.'
33            return [''.join(grid[i]) for i in range(m)]
34
35        if m >= k and n > 1:
36            for i in range(m-1, m-k-1, -1):
37                grid[i][1] = '.'
38            return [''.join(grid[i]) for i in range(m)]
39        elif n >= k and m > 1:
40            for i in range(k):
41                grid[m-2][i] = '.'
42            return [''.join(grid[i]) for i in range(m)]
43        else:
44            for mask in range(1, 1 << x):
45                if mask & 1 == 0: continue
46                rec.cache_clear()
47                g_mask = mask
48                if rec(0, 0) == k: 
49                    return generateGrid(mask)
50            
51            return []