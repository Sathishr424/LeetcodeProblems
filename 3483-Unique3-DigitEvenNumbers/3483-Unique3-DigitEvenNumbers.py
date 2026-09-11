# Last updated: 9/11/2026, 3:54:43 PM
1class Solution:
2    def totalNumbers(self, digits: List[int]) -> int:
3        n = len(digits)
4
5        uniq = set()
6        for i in range(n):
7            if digits[i] == 0: continue
8            for j in range(n):
9                if i == j: continue
10                for k in range(n):
11                    if k == i or k == j or digits[k] % 2: continue
12                    uniq.add(str(digits[i]) + str(digits[j]) + str(digits[k]))
13
14        return len(uniq)