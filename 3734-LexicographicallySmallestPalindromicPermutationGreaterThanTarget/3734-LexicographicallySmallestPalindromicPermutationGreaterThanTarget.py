# Last updated: 8/28/2026, 3:42:48 PM
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
27        odd = ""
28        for c in range(26):
29            if freq[c] % 2:
30                odd = chr(c + ord('a'))
31                break
32
33        def buildRem(index, curr):
34            while index < n // 2:
35                for c in range(26):
36                    if freq[c] > 1:
37                        freq[c] -= 2
38                        curr += chr(c + ord('a'))
39                        break
40                index += 1
41
42            return curr + odd
43
44        def rec(index, curr):
45            if n % 2:
46                if index == half - 1:
47                    c = ord(target[index]) - ord('a')
48
49                    if freq[c] == 1:
50                        curr += target[index]
51                        if isLargerRightHalf(curr): return curr
52                    else:
53                        c += 1
54                        while c < 26 and freq[c] != 1:
55                            c += 1
56
57                        if c < 26: return curr + chr(c + ord('a'))
58                    return ""
59            elif index == half:
60                if isLargerRightHalf(curr): return curr
61                return ""
62
63            c = ord(target[index]) - ord('a')
64
65            if freq[c] > 1:
66                freq[c] -= 2
67                best = rec(index + 1, curr + target[index])
68                if best != "": return best
69                freq[c] += 2
70
71            c += 1
72            while c < 26 and freq[c] <= 1:
73                c += 1
74
75            if c < 26: 
76                freq[c] -= 2
77                return buildRem(index + 1, curr + chr(c + ord('a')))
78            return ""
79
80        best = rec(0, "")
81        return best + best[:n//2][::-1]