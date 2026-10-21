# Last updated: 10/21/2026, 3:48:35 PM
1class Solution:
2    def minOperations(self, s: str) -> int:
3        n = len(s)
4        s = list(s)
5        orig_s = s[:]
6        sorted_s = sorted(s)
7        if n == 2 and s != sorted_s: return -1
8        if s == sorted_s: return 0
9
10        # Trying left first and right
11        ans = 0
12        left = s[:-1]
13        sorted_left = sorted(left)
14        if left != sorted_left:
15            ans += 1
16            s = sorted_left + [s[-1]]
17        right = s[1:]
18        sorted_right = sorted(right)
19        if right != sorted_right:
20            ans += 1
21            s = [s[0]] + sorted_right
22        if sorted_s != s: ans += 1
23
24        best = ans
25        # Trying right first and left
26        s = orig_s
27        ans = 0
28        right = s[1:]
29        sorted_right = sorted(right)
30        if right != sorted_right:
31            ans += 1
32            s = [s[0]] + sorted_right
33        left = s[:-1]
34        sorted_left = sorted(left)
35        if left != sorted_left:
36            ans += 1
37            s = sorted_left + [s[-1]]
38        if sorted_s != s: ans += 1
39
40        return min(best, ans)