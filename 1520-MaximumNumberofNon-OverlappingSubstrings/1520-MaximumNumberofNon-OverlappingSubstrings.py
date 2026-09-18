# Last updated: 9/18/2026, 2:59:45 PM
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
12        curr = [0] * 26
13        ans = []
14        last = 0
15        for i in range(n):
16            a = ord(s[i]) - ord('a')
17            curr[a] += 1
18
19            for b in range(26):
20                if curr[b]:
21                    if curr[b] != freq[b]: break
22            else:
23                ans.append(s[last:i + 1])
24                curr = [0] * 26
25                last = i + 1
26                continue
27
28            left = indexes[a]
29            if curr[a] == freq[a] and (i - left + 1) == freq[a]:
30                ans.append(s[left:i+1])
31                curr = [0] * 26
32                last = i + 1
33
34        if last < n:
35            for j in range(last, n):
36                if indexes[ord(s[j]) - ord('a')] < last: break
37            else:
38                ans.append(s[last:])
39
40        new_ans = []
41        for curr in ans:
42            while len(curr) > 2 and curr[0] == curr[-1]:
43                a = ord(curr[0]) - ord('a')
44                l = 0 
45                r = len(curr) - 1
46
47                while l < r and curr[l] == curr[0]:
48                    l += 1
49
50                while r > l and curr[r] == curr[-1]:
51                    r -= 1
52
53                cnt = l + (len(curr) - r - 1)
54                if cnt == freq[a]:
55                    curr = curr[l:r+1]
56                else:
57                    break
58            new_ans.append(curr)
59
60        return new_ans