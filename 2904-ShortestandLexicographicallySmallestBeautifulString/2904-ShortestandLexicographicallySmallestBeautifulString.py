# Last updated: 8/26/2026, 3:51:18 PM
1class Solution:
2    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
3        n = len(s)
4        if s.count('1') < k: return ""
5
6        best = ""
7        best_val = 1 << 100
8        for i in range(n-1, -1, -1):
9            one = 0
10            val = 0
11            power = 0
12            for j in range(i, -1, -1):
13                if s[j] == '1': 
14                    one += 1
15                    val += 1 << power
16                    if one == k:
17                        if val < best_val:
18                            best_val = val
19                            best = s[j:i+1]
20                        break
21                power += 1
22
23        return best