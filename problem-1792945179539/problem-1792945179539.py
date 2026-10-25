# Last updated: 10/25/2026, 9:49:39 PM
1class Solution:
2    def countMagicalPairs(self, s: str) -> int:
3        n = len(s)
4        alp = [ord(c) - ord('a') for c in s] 
5
6        there = [[0] * 27 for _ in range(n)]
7        ret = 0
8
9        for poss in range(1, 27):
10            freq = [0] * 26
11            cnt = 0
12
13            left = 0
14            pre = 0
15            curr = 0
16            for i in range(n):
17                freq[alp[i]] += 1
18                if freq[alp[i]] == 1:
19                    cnt += 1
20
21                if cnt > poss:
22                    pre = 0
23
24                while cnt > poss:
25                    freq[alp[left]] -= 1
26                    if freq[alp[left]] == 0: cnt -= 1
27                    left += 1
28
29                if cnt == poss:
30                    index = left
31                    while freq[alp[left]] > 1:
32                        freq[alp[left]] -= 1
33                        there[left][poss] += there[left - 1][poss]
34                        left += 1
35
36                    pre += left - index
37                    there[i][poss] = pre + 1
38                    if left > 0: curr += there[left - 1][poss]
39            # print(poss, curr)
40            ret += curr
41
42        # [print(row) for row in there]
43        return ret