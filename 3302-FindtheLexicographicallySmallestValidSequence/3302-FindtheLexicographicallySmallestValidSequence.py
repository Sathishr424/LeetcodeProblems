# Last updated: 8/8/2026, 3:37:06 PM
1from typing import List
2from bisect import bisect_left
3
4
5class Solution:
6    def validSequence(self, word1: str, word2: str) -> List[int]:
7        m = len(word1)
8        n = len(word2)
9
10        # Positions of every character in word1.
11        positions = [[] for _ in range(26)]
12        for i, ch in enumerate(word1):
13            positions[ord(ch) - ord('a')].append(i)
14
15        # run_start[i] = start of the consecutive run of word1[i].
16        #
17        # This lets us find the previous character that is NOT c
18        # in O(1), when word1[bound - 1] == c.
19        run_start = [0] * m
20        for i in range(m):
21            if i == 0 or word1[i] != word1[i - 1]:
22                run_start[i] = i
23            else:
24                run_start[i] = run_start[i - 1]
25
26        def prev_same(c: int, bound: int) -> int:
27            """Largest index < bound containing character c."""
28            arr = positions[c]
29            k = bisect_left(arr, bound)
30            return arr[k - 1] if k else -1
31
32        def prev_diff(c: int, bound: int) -> int:
33            """Largest index < bound whose character != c."""
34            if bound <= 0:
35                return -1
36
37            i = bound - 1
38
39            if ord(word1[i]) - ord('a') != c:
40                return i
41
42            # word1[i] == c.
43            # Skip the whole consecutive run of c.
44            return run_start[i] - 1
45
46        # exact[j]:
47        # Largest possible index for word2[j] such that
48        # word2[j:] can be matched EXACTLY.
49        #
50        # one_change[j]:
51        # Largest possible index for word2[j] such that
52        # word2[j:] can be matched with at most ONE mismatch.
53        exact = [-1] * (n + 1)
54        one_change = [-1] * (n + 1)
55
56        # Empty suffix can start after the last character.
57        exact[n] = m
58        one_change[n] = m
59
60        for j in range(n - 1, -1, -1):
61            c = ord(word2[j]) - ord('a')
62
63            # Match word2[j] exactly.
64            exact[j] = prev_same(c, exact[j + 1])
65
66            # Option 1:
67            # word1[i] == word2[j], and the remaining suffix
68            # can contain at most one mismatch.
69            match = prev_same(c, one_change[j + 1])
70
71            # Option 2:
72            # word1[i] != word2[j], so we spend our one mismatch.
73            # The rest must then match exactly.
74            mismatch = prev_diff(c, exact[j + 1])
75
76            one_change[j] = max(match, mismatch)
77
78        answer = []
79        prev = -1
80        used_change = False
81
82        for j, ch in enumerate(word2):
83            c = ord(ch) - ord('a')
84
85            # Smallest index > prev where word1[index] == word2[j].
86            arr = positions[c]
87            k = bisect_left(arr, prev + 1)
88            match = arr[k] if k < len(arr) else m
89
90            candidates = []
91
92            if not used_change:
93                # We can match this character and keep our
94                # one-change allowance for later.
95                if match < m and match < one_change[j + 1]:
96                    candidates.append((match, False))
97
98                # Or use our one allowed modification here.
99                mismatch = prev + 1
100
101                if mismatch < m and word1[mismatch] == ch:
102                    mismatch += 1
103
104                if mismatch < m and mismatch < exact[j + 1]:
105                    candidates.append((mismatch, True))
106
107            else:
108                # The modification has already been used,
109                # so everything from here must match exactly.
110                if match < m and match < exact[j + 1]:
111                    candidates.append((match, False))
112
113            if not candidates:
114                return []
115
116            # IMPORTANT:
117            # We choose the smallest INDEX, not the smallest
118            # resulting string.
119            index, uses_change = min(candidates)
120
121            answer.append(index)
122            prev = index
123            used_change |= uses_change
124
125        return answer