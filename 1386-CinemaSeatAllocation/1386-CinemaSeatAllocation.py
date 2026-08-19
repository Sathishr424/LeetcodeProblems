# Last updated: 8/19/2026, 5:58:28 AM
1choices = [[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8]]
2class Solution:
3    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
4        rows = defaultdict(lambda: [0] * 10)
5        for row, seat in reservedSeats:
6            rows[row][seat - 1] = 1
7
8        sorted_rows = sorted(rows.keys())
9        prev = 0
10        ans = 0
11        for row in sorted_rows:
12            diff = max(0, row - prev - 1)
13            ans += diff * 2
14            prev = row
15
16        diff = max(0, n - prev)
17        ans += diff * 2
18
19        for row in sorted_rows:
20            c = 0
21            while c < 3:
22                choice = choices[c]
23                for seat in choice:
24                    if rows[row][seat] == 1: break
25                else:
26                    ans += 1
27                    c += 1
28                c += 1
29
30        return ans