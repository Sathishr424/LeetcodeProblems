# Last updated: 8/9/2026, 7:09:36 PM
1class Solution:
2    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
3        n = len(source)
4        m = len(rules)
5        inf = 10**20
6
7        extra_costs = [0] * m
8        for i in range(m):
9            extra_costs[i] = rules[i][0].count('*')
10
11        @cache
12        def rec(index):
13            if index == n: return 0
14
15            ans = inf
16            if source[index] == target[index]:
17                ans = min(ans, rec(index + 1))
18
19            for i in range(m):
20                k = len(rules[i][0])
21                if index + k > n: continue
22                for j in range(k):
23                    if not ((rules[i][0][j] == '*' or source[index + j] == rules[i][0][j]) and rules[i][1][j] == target[index + j]):
24                        break
25                else:
26                    ans = min(ans, rec(index + k) + costs[i] + extra_costs[i])
27
28            return ans
29        
30        ans = rec(0)
31        rec.cache_clear()
32        return -1 if ans >= inf else ans