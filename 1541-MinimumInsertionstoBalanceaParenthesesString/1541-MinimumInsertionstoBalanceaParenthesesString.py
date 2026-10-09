# Last updated: 10/9/2026, 7:01:02 PM
1class Solution:
2    def minInsertions(self, s: str) -> int:
3        opening = 0
4        need = 0
5        for i, char in enumerate(s):
6            # print(i, char, opening, need)
7            if char == '(':
8                if opening % 2:
9                    need += 1
10                    opening -= 1
11                opening += 2
12            else:
13                if opening == 0:
14                    need += 1
15                    opening += 1
16                else:
17                    opening -= 1
18
19        return opening + need