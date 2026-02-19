# Last updated: 2/19/2026, 10:48:20 PM
1from typing import List
2
3class Solution:
4    def miceAndCheese(self, r1: List[int], r2: List[int], k: int) -> int:
5        n = len(r1)
6
7        tot = sum(r2)
8
9        diff = []
10        for i in range(n):
11            diff.append(r2[i] - r1[i])
12
13        diff.sort()
14        return tot - sum(diff[:k])