# Last updated: 9/25/2026, 6:59:40 PM
1class Solution:
2    def braceExpansionII(self, expression: str) -> list[str]:
3        n = len(expression)
4
5        pairs = [-1] * n
6        open = []
7        for i in range(n):
8            if expression[i] == '{':
9                open.append(i)
10            elif expression[i] == '}':
11                pairs[open.pop()] = i
12
13        def getAll(arr):
14            res = []
15            for val in arr:
16                if type(val) == list:
17                    res += getAll(val)
18                else:
19                    if val != ",":
20                        res.append(val)
21            return res
22
23        def getComb(x, y):
24            left = getAll(x)
25            right = getAll(y)
26
27            comb = []
28            for l in left:
29                for r in right:
30                    comb.append(str(l) + str(r))
31
32            return comb
33
34        def rec(l, r):
35            i = l
36            curr = ''
37            res = []
38            while i <= r:
39                if expression[i] == '{':
40                    curr_res = rec(i + 1, pairs[i] - 1)
41
42                    if curr:
43                        if res and res[-1] != ',':
44                            res[-1] = getComb(res[-1], [curr])
45                            res[-1] = getComb(res[-1], curr_res)
46                        else:
47                            res.append(getComb([curr], curr_res))
48                    elif res and res[-1] != ',':
49                        res[-1] = getComb(res[-1], curr_res)
50                    else:
51                        res.append(curr_res)
52                    curr = ''
53                    i = pairs[i]
54                elif expression[i] == ',':
55                    if curr:
56                        if res and res[-1] != ',':
57                            res[-1] = getComb(res[-1], [curr])
58                        elif curr:
59                            res.append(curr)
60                    elif res and res[-1] != ',':
61                        res += getAll(res.pop())
62                    res.append(',')
63                    curr = ''
64                else:
65                    curr += expression[i]
66                i += 1
67
68            if curr:
69                if res and res[-1] != ',':
70                    res[-1] = getComb(res[-1], [curr])
71                else:
72                    res.append(curr)
73
74            return res
75
76        res = rec(0, n-1)
77        if type(res[-1]) == list: res += getAll(res.pop())
78
79        return sorted(set(res))