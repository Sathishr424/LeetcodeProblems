# Last updated: 12/16/2025, 10:46:14 PM
1class Solution:
2    def maxProfit(
3        self,
4        n: int,
5        present: List[int],
6        future: List[int],
7        hierarchy: List[List[int]],
8        budget: int,
9    ) -> int:
10        g = [[] for _ in range(n)]
11        for e in hierarchy:
12            g[e[0] - 1].append(e[1] - 1)
13
14        def dfs(u: int):
15            cost = present[u]
16            dCost = present[u] // 2
17
18            # dp[u][state][budget]
19            # state = 0: Do not purchase parent node, state = 1: Must purchase parent node
20            dp0 = [0] * (budget + 1)
21            dp1 = [0] * (budget + 1)
22
23            # subProfit[state][budget]
24            # state = 0: discount not available, state = 1: discount available
25            subProfit0 = [0] * (budget + 1)
26            subProfit1 = [0] * (budget + 1)
27            uSize = cost
28
29            for v in g[u]:
30                child_dp0, child_dp1, vSize = dfs(v)
31                uSize += vSize
32                for i in range(budget, -1, -1):
33                    for sub in range(min(vSize, i) + 1):
34                        if i - sub >= 0:
35                            subProfit0[i] = max(
36                                subProfit0[i],
37                                subProfit0[i - sub] + child_dp0[sub],
38                            )
39                            subProfit1[i] = max(
40                                subProfit1[i],
41                                subProfit1[i - sub] + child_dp1[sub],
42                            )
43
44            for i in range(budget + 1):
45                dp0[i] = subProfit0[i]
46                dp1[i] = subProfit0[i]
47                if i >= dCost:
48                    dp1[i] = max(
49                        subProfit0[i], subProfit1[i - dCost] + future[u] - dCost
50                    )
51                if i >= cost:
52                    dp0[i] = max(
53                        subProfit0[i], subProfit1[i - cost] + future[u] - cost
54                    )
55
56            return dp0, dp1, uSize
57
58        return dfs(0)[0][budget]