# Last updated: 8/28/2026, 1:32:38 AM
1class Solution:
2    def lexGreaterPermutation(self, s: str, target: str) -> str:
3        n = len(s)
4
5        freq = [0] * 26
6        for char in s:
7            freq[ord(char) - ord('a')] += 1
8
9        def buildSmall(curr):
10            for c in range(26):
11                for _ in range(freq[c]):
12                    curr += chr(c + ord('a'))
13            return curr
14
15        def rec(index, curr):
16            if index == n:
17                return ""
18            
19            c = ord(target[index]) - ord('a')
20            if freq[c]:
21                freq[c] -= 1
22                best = rec(index + 1, curr + chr(c + ord('a')))
23                if best != "": return best
24                freq[c] += 1
25
26            c += 1
27            while c < 26 and freq[c] == 0:
28                c += 1
29
30            if c < 26:
31                freq[c] -= 1
32                return buildSmall(curr + chr(c + ord('a')))
33
34            return ""
35
36        return rec(0, "")