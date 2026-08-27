# Last updated: 8/28/2026, 1:26:41 AM
1class Solution:
2    def lexGreaterPermutation(self, s: str, target: str) -> str:
3        n = len(s)
4
5        z = "z" * (n + 1)
6        freq = [0] * 26
7        for char in s:
8            freq[ord(char) - ord('a')] += 1
9
10
11        def buildSmall(index, curr):
12            while index < n:
13                for c in range(26):
14                    for _ in range(freq[c]):
15                        curr += chr(c + ord('a'))
16                        index += 1
17            return curr
18
19        def rec(index, curr):
20            if index == n:
21                return z
22            
23            c = ord(target[index]) - ord('a')
24            best = z
25            if freq[c]:
26                freq[c] -= 1
27                best = rec(index + 1, curr + chr(c + ord('a')))
28                freq[c] += 1
29
30            c += 1
31            while c < 26 and freq[c] == 0:
32                c += 1
33
34            if c < 26:
35                freq[c] -= 1
36                best = min(best, buildSmall(index + 1, curr + chr(c + ord('a'))))
37                freq[c] += 1
38
39            return best
40
41        ans = rec(0, "")
42        return ans if ans != z else ""