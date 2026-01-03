# Last updated: 1/3/2026, 2:04:15 PM
1class Solution:
2    def numOfWays(self, n: int) -> int:
3        mod = 10**9 + 7
4        vals = []
5        stack = ["0", "1", "2"]
6        while stack:
7            prev = stack.pop()
8            if len(prev) == 3:
9                vals.append(prev)
10                continue
11            for i in range(3):
12                if str(i) != prev[-1]:
13                    stack.append(prev + str(i))
14            
15        graph = defaultdict(list)
16        m = len(vals)
17        for i in range(m):
18            x = vals[i]
19            for j in range(i+1, m):
20                y = vals[j]
21
22                if x[0] != y[0] and x[1] != y[1] and x[2] != y[2]:
23                    graph[x].append(y)
24                    graph[y].append(x)
25
26
27        @cache
28        def rec(x, rem):
29            if rem == 0: return 1
30            ans = 0
31            for y in graph[x]:
32                ans += rec(y, rem - 1)
33            return ans % mod
34
35        ans = 0
36        for val in vals:
37            ans += rec(val, n-1)
38            ans %= mod
39        
40        rec.cache_clear()
41        return ans