# Last updated: 11/9/2026, 11:53:59 PM
1class Solution:
2    def countValidSubstrings(self, s: str) -> int:
3        n = len(s)
4        total = (n * (n + 1)) // 2
5
6        bs = [-1] * n
7        c = -1
8        b = -1
9        for i in range(n-1, -1, -1):
10            if s[i] == 'c':
11                c = i
12            elif s[i] == 'b':
13                if c != -1:
14                    b = c
15            bs[i] = b
16        # print(bs)
17
18        ans = 0
19        last_a = -1
20        for i in range(n):
21            if s[i] == 'a':
22                index = bs[i]
23                if index != -1:
24                    curr = (n - index) * (i - last_a)
25                    # print(i, index, (n-index, i - last_a), curr)
26                    ans += curr
27                    last_a = i
28
29        # print(total, ans)
30        return total - ans