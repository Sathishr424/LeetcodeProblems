# Last updated: 9/18/2026, 11:20:07 AM
1class Solution:
2    def maxArea(self, mat: List[List[int]]) -> int:
3        m = len(mat)
4        n = len(mat[0])
5
6        inf = 10**20
7
8        dp = [[mat[i][j] for j in range(n)] for i in range(m)]
9        reverse_dp = [[mat[i][j] for j in range(n)] for i in range(m)]
10        DIR = [[-1, 0], [0, -1], [-1, -1]]
11        REVERSE_DIR = [[1, 0], [0, 1], [1, 1]]
12
13        cnt = sum([sum(mat[i]) for i in range(m)])
14        if cnt <= 1: return 0
15        ans = 1
16        for i in range(1, m):
17            for j in range(1, n):
18                if dp[i][j] == 0: continue
19                mn = inf
20                for i2, j2 in DIR:
21                    i2 += i
22                    j2 += j
23                    mn = min(mn, dp[i2][j2])
24
25                dp[i][j] = mn + 1
26
27        for i in range(m-2, -1, -1):
28            for j in range(n-2, -1, -1):
29                if reverse_dp[i][j] == 0: continue
30                mn = inf
31                for i2, j2 in REVERSE_DIR:
32                    i2 += i
33                    j2 += j
34                    mn = min(mn, reverse_dp[i2][j2])
35
36                reverse_dp[i][j] = mn + 1
37
38        # [print(row) for row in dp]
39        # print()
40        # [print(row) for row in reverse_dp]
41
42        prefix = [0] * (n+1)
43        suffix = [0] * (n+1)
44        for j in range(n):
45            mx = 0
46            for i in range(m):
47                mx = max(mx, dp[i][j])
48            prefix[j] = max(prefix[j-1], mx)
49                
50        for j in range(n-1, 0, -1):
51            mx = 0
52            for i in range(m):
53                mx = max(mx, reverse_dp[i][j])
54            suffix[j] = max(suffix[j+1], mx)
55            ans = max(ans, min(prefix[j-1], suffix[j]))
56
57
58        prefix = [0] * (m+1)
59        suffix = [0] * (m+1)
60        for i in range(m):
61            mx = 0
62            for j in range(n):
63                mx = max(mx, dp[i][j])
64            prefix[i] = max(prefix[i-1], mx)
65                
66        for i in range(m-1, 0, -1):
67            mx = 0
68            for j in range(n):
69                mx = max(mx, reverse_dp[i][j])
70            suffix[i] = max(suffix[i+1], mx)
71            ans = max(ans, min(prefix[i-1], suffix[i]))
72
73        return ans * ans