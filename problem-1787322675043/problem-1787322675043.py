# Last updated: 8/21/2026, 8:01:15 PM
1class Solution:
2    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
3        n = len(monsters)
4
5        diff = [0] * (n + 1)
6        for l, r, b in boosts:
7            diff[l] += b
8            diff[r + 1] -= b
9
10        curr = 0
11        bonus = [0] * n
12        for i in range(n):
13            curr += diff[i]
14            bonus[i] = curr
15
16        l = 0
17        r = 10**20
18
19        while l < r:
20            mid = (l + r) // 2
21            
22            strength = mid
23            for i in range(n):
24                curr = strength + bonus[i]
25                if curr < monsters[i]: 
26                    l = mid + 1
27                    break
28                strength = max(0, strength - monsters[i])
29            else:
30                r = mid
31
32        return l
33
34        # needed = []
35        # for i in range(n):
36        #     need = max(0, monsters[i] - bonus[i])
37        #     needed.append(need)
38
39        # print(monsters)
40        # print(bonus)
41        # print(needed)