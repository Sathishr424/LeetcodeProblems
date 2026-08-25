# Last updated: 8/25/2026, 1:53:28 PM
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
30                if left > right:
31                    if alice:
32                        if left_q:
33                            left += 9
34                            left_q -= 1
35                        else:
36                            right_q -= 1
37                    else:
38                        if right_q:
39                            right += 9
40                            right_q -= 1
41                        else:
42                            left_q -= 1
43                elif right > left:
44                    if not alice:
45                        if left_q:
46                            left += 9
47                            left_q -= 1
48                        else:
49                            right_q -= 1
50                    else:
51                        if right_q:
52                            right += 9
53                            right_q -= 1
54                        else:
55                            left_q -= 1
56                else:
57                    if alice:
58                        if left_q:
59                            left += 9
60                            left_q -= 1
61                        else:
62                            right += 9
63                            right_q -= 1
64                    else:
65                        if left_q: left_q -= 1
66                        else: right_q -= 1
67                rem -= 1
68                alice = not alice
69
70            return left != right
71
72        return True