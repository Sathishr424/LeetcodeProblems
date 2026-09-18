# Last updated: 9/18/2026, 3:06:21 PM
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
13        ranges = []
14        last = 0
15        for i in range(n):
16            a = ord(s[i]) - ord('a')
17            curr[a] += 1
18
19            for b in range(26):
20                if curr[b]:
21                    if curr[b] != freq[b]: break
22            else:
23                ranges.append((last, i))
24                curr = [0] * 26
25                last = i + 1
26                continue
27
28            left = indexes[a]
29            if curr[a] == freq[a] and (i - left + 1) == freq[a]:
30                ranges.append((left, i))
31                curr = [0] * 26
32                last = i + 1
33
34        if last < n:
35            for j in range(last, n):
36                if indexes[ord(s[j]) - ord('a')] < last: break
37            else:
38                ranges.append((last, n-1))
39
40        ans = []
41        for l, r in ranges:
42            while r - l > 1 and s[l] == s[r]:
43                match = s[l]
44                L = l
45                R = r
46                a = ord(s[l]) - ord('a')
47
48                while l < r and s[l] == match:
49                    l += 1
50
51                while r > l and s[r] == match:
52                    r -= 1
53
54                cnt = (l - L) + (R - r)
55                if cnt != freq[a]:
56                    l = L
57                    r = R
58                    break
59            ans.append(s[l:r+1])
60
61        return ans