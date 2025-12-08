# Last updated: 12/8/2025, 6:52:25 PM
1from typing import List
2
3class Solution:
4    def isGood(self, target: int, ranks: List[int], cars: int) -> bool:
5        for rank in ranks:
6            cars -= floor(sqrt(target // rank))
7        return cars <= 0
8    
9    def repairCars(self, ranks: List[int], cars: int) -> int:
10        n = len(ranks)
11        ranks.sort()
12
13        l = 1
14        r = ranks[n - 1] * cars * cars
15
16        while l < r:
17            mid = (l + r) // 2
18
19            if self.isGood(mid, ranks, cars):
20                r = mid
21            else:
22                l = mid + 1
23
24        return l
25