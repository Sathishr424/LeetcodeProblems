# Last updated: 8/25/2026, 2:01:03 PM
1class Solution:
2    def sumGame(self, num: str) -> bool:
3        n = len(num)
4
5        mid = n // 2
6
7        left = 0
8        left_q = 0
9        right = 0
10        right_q = 0
11        for i in range(mid):
12            if num[i] == '?':
13                left_q += 1
14            else:
15                left += int(num[i])
16
17        for i in range(mid, n):
18            if num[i] == '?':
19                right_q += 1
20            else:
21                right += int(num[i])
22
23        if left == right:
24            if left_q == right_q: return False
25
26        rem = left_q + right_q
27        if rem % 2 == 0:
28            alice = True
29            while rem:
30                if left != right:
31                    condition = (left > right and alice) or (not alice and right > left)
32                    if condition:
33                        if left_q:
34                            left += 9
35                            left_q -= 1
36                        else:
37                            right_q -= 1
38                    else:
39                        if right_q:
40                            right += 9
41                            right_q -= 1
42                        else:
43                            left_q -= 1
44                else:
45                    if alice:
46                        if left_q:
47                            left += 9
48                            left_q -= 1
49                        else:
50                            right += 9
51                            right_q -= 1
52                    else:
53                        if left_q: left_q -= 1
54                        else: right_q -= 1
55                rem -= 1
56                alice = not alice
57
58            return left != right
59
60        return True