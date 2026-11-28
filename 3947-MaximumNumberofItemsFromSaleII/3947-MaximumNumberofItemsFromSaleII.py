# Last updated: 11/28/2026, 3:02:04 PM
1def count_divisibles(arr):
2    mx = max(arr)
3    freq = [0] * (mx + 1)
4
5    for x in arr:
6        freq[x] += 1
7
8    ans = [0] * (mx + 1)
9    for x in range(1, mx + 1):
10        for multiple in range(x, mx + 1, x):
11            ans[x] += freq[multiple]
12
13    return [ans[x]-1 for x in arr]
14
15class Solution:
16    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
17        mn = min([p for _, p in items])
18
19        free = count_divisibles([f for f, _ in items])
20
21        stack = []
22        for i, (f, p) in enumerate(items):
23            if free[i] == 0 or mn * 2 <= p: continue
24            stack.append((p, free[i]))
25
26        stack.sort()
27        ans = 0
28        for p, f in stack:
29            if p > budget: break
30            can = min(f, budget // p)
31            ans += can * 2
32            budget -= can * p
33
34        return ans + budget // mn