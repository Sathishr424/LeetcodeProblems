# Last updated: 10/28/2026, 9:34:04 PM
1class Solution:
2    def minOperations(self, s: str) -> int:
3        # "abc" -> "abcabc"
4        n = len(s)
5        inf = 10**9
6
7        double = [ord(c) - ord('a') for c in s]
8        double += double
9        # print(double)
10
11        half = n // 2
12        best = inf
13        for i in range(n):
14            right = i + n - 1
15            curr = i
16            for j in range(i, i + half):
17                l = double[j]
18                r = double[right - (j - i)]
19
20                curr += min((l - r) % 26, (r - l) % 26)
21            best = min(best, curr)
22
23        return best