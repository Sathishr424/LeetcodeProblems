# Last updated: 8/19/2026, 5:57:00 AM
1class Solution:
2    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
3        reservedSeats.sort(key=lambda x: x[1])
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
19        choices = [[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8]]
20        for row in sorted_rows:
21            c = 0
22            while c < 3:
23                choice = choices[c]
24                for seat in choice:
25                    if rows[row][seat] == 1: break
26                else:
27                    ans += 1
28                    c += 1
29                c += 1
30
31        return ans