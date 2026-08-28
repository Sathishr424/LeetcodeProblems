# Last updated: 8/28/2026, 3:40:40 PM
1class Solution:
2    def lexPalindromicPermutation(self, s: str, target: str) -> str:
3        n = len(s)
4        half = (n + 1) // 2
5
6        freq = [0] * 26
7        for char in s:
8            freq[ord(char) - ord('a')] += 1
9
10        odd = 0
11        even = 0
12        for c in range(26):
13            if freq[c]:
14                odd += freq[c] % 2
15                even += freq[c] % 2 == 0
16
17        if (n % 2 and odd > 1) or (n % 2 == 0 and odd): return ""
18
19        def isLargerRightHalf(curr):
20            for i in range(half, n):
21                left = n - i - 1
22                if curr[left] > target[i]: return True
23                elif curr[left] < target[i]: return False
24
25            return False
26
27        def buildRem(index, curr):
28            odd = ""
29            for c in range(26):
30                if freq[c] % 2:
31                    odd = chr(c + ord('a'))
32                    break
33
34            while index < n // 2:
35                for c in range(26):
36                    if freq[c] > 1:
37                        freq[c] -= 2
38                        curr += chr(c + ord('a'))
39                        break
40                index += 1
41
42            if n % 2:
43                curr += odd
44
45            return curr
46
47        def rec(index, curr):
48            if n % 2:
49                if index == half - 1:
50                    orig = ord(target[index]) - ord('a')
51                    c = orig
52
53                    if freq[c] == 1:
54                        curr += target[index]
55                        if isLargerRightHalf(curr): return curr
56                    else:
57                        c += 1
58                        while c < 26 and freq[c] != 1:
59                            c += 1
60
61                        if c < 26: return curr + chr(c + ord('a'))
62                    return ""
63            elif index == half:
64                if isLargerRightHalf(curr): return curr
65                return ""
66
67            orig = ord(target[index]) - ord('a')
68            c = orig
69
70            if freq[c] > 1:
71                freq[c] -= 2
72                best = rec(index + 1, curr + target[index])
73                if best != "": return best
74                freq[c] += 2
75
76            c += 1
77            while c < 26 and freq[c] <= 1:
78                c += 1
79
80            if c < 26: 
81                freq[c] -= 2
82                return buildRem(index + 1, curr + chr(c + ord('a')))
83            return ""
84
85        best = rec(0, "")
86        # print('half', best)
87        return best + best[:n//2][::-1]