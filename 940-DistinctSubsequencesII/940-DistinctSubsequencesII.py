# Last updated: 9/7/2026, 9:29:13 PM
1class Solution:
2    def distinctSubseqII(self, s: str) -> int:
3        n = len(s)
4        mod = 10**9 + 7
5
6        @cache
7        def rec(index, prev):
8            if index == n:
9                return 1 if prev != '' else 0
10            ans = rec(index + 1, prev)
11            if s[index] == prev: return ans
12            
13            curr = index
14            while curr < n and s[curr] == s[index]:
15                curr += 1
16
17            ans += rec(curr, s[index])
18            return ans % mod
19        
20        ans = rec(0, '')
21        rec.cache_clear()
22        return ans