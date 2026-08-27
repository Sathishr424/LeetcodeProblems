# Last updated: 8/28/2026, 1:31:55 AM
1class Solution:
2    def lexGreaterPermutation(self, s: str, target: str) -> str:
3        n = len(s)
4
5        freq = [0] * 26
6        for char in s:
7            freq[ord(char) - ord('a')] += 1
8
9        def buildSmall(index, curr):
10            for c in range(26):
11                for _ in range(freq[c]):
12                    curr += chr(c + ord('a'))
13                    index += 1
14            return curr
15
16        def rec(index, curr):
17            if index == n:
18                return ""
19            
20            c = ord(target[index]) - ord('a')
21            if freq[c]:
22                freq[c] -= 1
23                best = rec(index + 1, curr + chr(c + ord('a')))
24                if best != "": return best
25                freq[c] += 1
26
27            c += 1
28            while c < 26 and freq[c] == 0:
29                c += 1
30
31            if c < 26:
32                freq[c] -= 1
33                return buildSmall(index + 1, curr + chr(c + ord('a')))
34
35            return ""
36
37        return rec(0, "")