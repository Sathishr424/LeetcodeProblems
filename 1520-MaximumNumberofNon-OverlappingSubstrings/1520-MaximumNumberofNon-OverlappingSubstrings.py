# Last updated: 9/18/2026, 2:58:07 PM
1class Solution:
2    def maxNumOfSubstrings(self, s: str) -> list[str]:
3        n = len(s)
4        freq = [0] * 26
5        indexes = [-1] * 26
6        for i, c in enumerate(s):
7            a = ord(c) - ord('a')
8            freq[a] += 1
9            if indexes[a] == -1:
10                indexes[a] = i
11
12        cannot_add = [0] * 26
13        curr = [0] * 26
14        ans = []
15        last = 0
16        for i in range(n):
17            a = ord(s[i]) - ord('a')
18            curr[a] += 1
19
20            for b in range(26):
21                if curr[b]:
22                    if curr[b] != freq[b]: break
23            else:
24                ans.append(s[last:i + 1])
25                curr = [0] * 26
26                last = i + 1
27                continue
28
29            left = indexes[a]
30            if curr[a] == freq[a] and (i - left + 1) == freq[a]:
31                ans.append(s[left:i+1])
32                for b in range(26):
33                    if b == a: continue
34                    cannot_add[b] = 1
35                curr = [0] * 26
36                last = i + 1
37
38        if last < n:
39            for j in range(last, n):
40                if cannot_add[ord(s[j]) - ord('a')]: break
41            else:
42                ans.append(s[last:])
43
44        new_ans = []
45        for curr in ans:
46            while len(curr) > 2 and curr[0] == curr[-1]:
47                a = ord(curr[0]) - ord('a')
48                l = 0 
49                r = len(curr) - 1
50
51                while l < r and curr[l] == curr[0]:
52                    l += 1
53
54                while r > l and curr[r] == curr[-1]:
55                    r -= 1
56
57                cnt = l + (len(curr) - r - 1)
58                if cnt == freq[a]:
59                    curr = curr[l:r+1]
60                else:
61                    break
62            new_ans.append(curr)
63
64        return new_ans