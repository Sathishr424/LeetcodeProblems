# Last updated: 8/28/2026, 1:23:48 AM
1class Solution:
2    def lexGreaterPermutation(self, s: str, target: str) -> str:
3        n = len(s)
4
5        freq = [0] * 26
6        for char in s:
7            freq[ord(char) - ord('a')] += 1
8
9        z = "z" * (n + 1)
10
11        def buildSmall(index, curr):
12            tmp = freq[:]
13            for i in range(index, n):
14                for c in range(26):
15                    if tmp[c]:
16                        curr += chr(c + ord('a'))
17                        tmp[c] -= 1
18                        break
19            return curr
20
21        def rec(index, curr):
22            if index == n:
23                return z
24            
25            c = ord(target[index]) - ord('a')
26            best = z
27            if freq[c]:
28                freq[c] -= 1
29                best = rec(index + 1, curr + chr(c + ord('a')))
30                freq[c] += 1
31
32            c += 1
33            while c < 26 and freq[c] == 0:
34                c += 1
35
36            if c < 26:
37                freq[c] -= 1
38                best = min(best, buildSmall(index + 1, curr + chr(c + ord('a'))))
39                freq[c] += 1
40
41            return best
42
43        ans = rec(0, "")
44        return ans if ans != z else ""