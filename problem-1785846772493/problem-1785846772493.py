# Last updated: 8/4/2026, 6:02:52 PM
1class Solution:
2    def canMakeSubsequence(self, s: str, t: str) -> bool:
3        m = len(s)
4        n = len(t)
5        if n < m: return False
6
7        index = 0
8        found = [0] * n
9        matched = [-1] * n
10        for i in range(n):
11            if index < m and s[index] == t[i]:
12                matched[i] = index
13                index += 1
14            found[i] = index
15
16        if index == m: return True
17
18        index = m-1
19        for i in range(n-1, -1, -1):
20            if t[i] == s[index]:
21                index -= 1
22            elif found[i] == index and matched[i] == -1:
23                return True
24
25        return False