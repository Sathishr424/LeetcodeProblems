# Last updated: 8/28/2026, 1:27:37 AM
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
12            for c in range(26):
13                for _ in range(freq[c]):
14                    curr += chr(c + ord('a'))
15                    index += 1
16            return curr
17
18        def rec(index, curr):
19            if index == n:
20                return z
21            
22            c = ord(target[index]) - ord('a')
23            best = z
24            if freq[c]:
25                freq[c] -= 1
26                best = rec(index + 1, curr + chr(c + ord('a')))
27                freq[c] += 1
28
29            c += 1
30            while c < 26 and freq[c] == 0:
31                c += 1
32
33            if c < 26:
34                freq[c] -= 1
35                best = min(best, buildSmall(index + 1, curr + chr(c + ord('a'))))
36                freq[c] += 1
37
38            return best
39
40        ans = rec(0, "")
41        return ans if ans != z else ""