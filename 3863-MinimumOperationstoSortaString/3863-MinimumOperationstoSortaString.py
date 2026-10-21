# Last updated: 10/21/2026, 3:43:18 PM
1class Solution:
2    def minOperations(self, s: str) -> int:
3        # cba
4        # bca
5        # bac
6        # abc
7
8        s = list(s)
9        orig_s = s[:]
10        sorted_s = sorted(s)
11        if s == sorted_s: return 0
12
13        # Trying left first and right
14        ans = 0
15        left = s[:-1]
16        if left != sorted(left):
17            ans += 1
18            s = sorted(left) + [s[-1]]
19        right = s[1:]
20        if right != sorted(right):
21            ans += 1
22            s = [s[0]] + sorted(right)
23        if ans == 0 and s != sorted_s: return -1
24        if sorted_s != s: ans += 1
25
26        best = ans
27        # Trying right first and left
28        s = orig_s
29        ans = 0
30        right = s[1:]
31        if right != sorted(right):
32            ans += 1
33            s = [s[0]] + sorted(right)
34        left = s[:-1]
35        if left != sorted(left):
36            ans += 1
37            s = sorted(left) + [s[-1]]
38        if ans == 0 and s != sorted_s: return -1
39        if sorted_s != s: ans += 1
40
41        return min(best, ans)