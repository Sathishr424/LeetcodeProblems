# Last updated: 1/3/2026, 2:07:46 PM
1mod = 10**9 + 7
2vals = []
3stack = ["0", "1", "2"]
4while stack:
5    prev = stack.pop()
6    if len(prev) == 3:
7        vals.append(prev)
8        continue
9    for i in range(3):
10        if str(i) != prev[-1]:
11            stack.append(prev + str(i))
12    
13graph = defaultdict(list)
14m = len(vals)
15for i in range(m):
16    x = vals[i]
17    for j in range(i+1, m):
18        y = vals[j]
19
20        if x[0] != y[0] and x[1] != y[1] and x[2] != y[2]:
21            graph[x].append(y)
22            graph[y].append(x)
23
24@cache
25def rec(x, rem):
26    if rem == 0: return 1
27    ans = 0
28    for y in graph[x]:
29        ans += rec(y, rem - 1)
30    return ans % mod
31
32for val in vals: rec(val, 4999)
33
34class Solution:
35    def numOfWays(self, n: int) -> int:
36        ans = 0
37        for val in vals:
38            ans += rec(val, n-1)
39            ans %= mod
40        
41        return ans