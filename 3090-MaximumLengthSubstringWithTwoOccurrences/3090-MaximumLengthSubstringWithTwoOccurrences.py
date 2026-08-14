# Last updated: 8/14/2026, 9:19:48 AM
1class Solution:
2    def maximumLengthSubstring(self, s: str) -> int:
3        n = len(s)
4
5        cnt = 0
6        freq = defaultdict(int)
7
8        best = 0
9        left = 0
10        for i in range(n):
11            freq[s[i]] += 1
12            if freq[s[i]] == 1: cnt += 1
13
14            while freq[s[i]] > 2:
15                freq[s[left]] -= 1
16                if freq[s[left]] == 0:
17                    cnt -= 1
18                left += 1
19
20            window = (i - left + 1)
21            best = max(best, window)
22
23        return best