# Last updated: 8/19/2026, 6:35:17 AM
1class Solution:
2    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
3        left, middle, right = 0b0111100000, 0b0001111000, 0b0000011110
4        rows = defaultdict(int)
5        for row, seat in reservedSeats:
6            rows[row] |= 1 << (seat - 1)
7
8        ans = (n - len(rows)) * 2
9        for row in rows.values():
10            # print(format(row & left, '010b'), format(row & middle, '010b'), format(row & right, '010b'))
11            if row & left == 0 and row & right == 0:
12                ans += 2
13            elif row & left == 0:
14                ans += 1
15            elif row & right == 0:
16                ans += 1
17            elif row & middle == 0:
18                ans += 1
19            # print(format(row, '010b'), ans)
20
21        return ans