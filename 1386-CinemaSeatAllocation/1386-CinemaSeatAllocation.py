# Last updated: 8/19/2026, 5:58:05 AM
1class Solution:
2    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
3        rows = defaultdict(lambda: [0] * 10)
4        for row, seat in reservedSeats:
5            rows[row][seat - 1] = 1
6
7        sorted_rows = sorted(rows.keys())
8        prev = 0
9        ans = 0
10        for row in sorted_rows:
11            diff = max(0, row - prev - 1)
12            ans += diff * 2
13            prev = row
14
15        diff = max(0, n - prev)
16        ans += diff * 2
17
18        choices = [[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8]]
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