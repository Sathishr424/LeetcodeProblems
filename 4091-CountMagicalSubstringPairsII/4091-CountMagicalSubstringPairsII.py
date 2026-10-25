# Last updated: 10/25/2026, 9:56:19 PM
1class Solution:
2    def countMagicalPairs(self, s: str) -> int:
3        n = len(s)
4        alp = [ord(c) - ord('a') for c in s] 
5
6        there = [[0] * 27 for _ in range(n + 1)]
7        ret = 0
8
9        for poss in range(1, 27):
10            freq = [0] * 26
11            cnt = 0
12
13            left = 0
14            pre = 0
15            for i in range(n):
16                freq[alp[i]] += 1
17                if freq[alp[i]] == 1:
18                    cnt += 1
19
20                if cnt > poss:
21                    pre = 0
22
23                while cnt > poss:
24                    freq[alp[left]] -= 1
25                    if freq[alp[left]] == 0: cnt -= 1
26                    left += 1
27
28                if cnt == poss:
29                    index = left
30                    while freq[alp[left]] > 1:
31                        freq[alp[left]] -= 1
32                        there[left][poss] += there[left - 1][poss]
33                        left += 1
34
35                    pre += left - index
36                    there[i][poss] = pre + 1
37                    ret += there[left - 1][poss]
38
39        return ret