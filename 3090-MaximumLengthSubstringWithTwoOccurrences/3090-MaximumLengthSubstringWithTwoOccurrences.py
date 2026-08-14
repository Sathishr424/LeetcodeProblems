# Last updated: 8/14/2026, 9:22:28 AM
1class Solution:
2    def maximumLengthSubstring(self, s: str) -> int:
3        n = len(s)
4        array = [ord(a) - ord('a') for a in s]
5
6        cnt = 0
7        freq = [0] * 26
8
9        best = 0
10        left = 0
11        for i in range(n):
12            freq[array[i]] += 1
13            if freq[array[i]] == 1: cnt += 1
14
15            while freq[array[i]] > 2:
16                freq[array[left]] -= 1
17                if freq[array[left]] == 0:
18                    cnt -= 1
19                left += 1
20
21            best = max(best, i - left + 1)
22
23        return best