# Last updated: 3/12/2025, 11:45:41 pm
1class Solution:
2    def countTrapezoids(self, points: List[List[int]]) -> int:
3        n = len(points)
4        inf = 10**9 + 7
5        slope_to_intercept = defaultdict(list)
6        mid_to_slope = defaultdict(list)
7        ans = 0
8
9        for i in range(n):
10            x1, y1 = points[i]
11            for j in range(i + 1, n):
12                x2, y2 = points[j]
13                dx = x1 - x2
14                dy = y1 - y2
15
16                if x2 == x1:
17                    k = inf
18                    b = x1
19                else:
20                    k = (y2 - y1) / (x2 - x1)
21                    b = (y1 * dx - x1 * dy) / dx
22
23                mid = (x1 + x2) * 10000 + (y1 + y2)
24                slope_to_intercept[k].append(b)
25                mid_to_slope[mid].append(k)
26
27        for sti in slope_to_intercept.values():
28            if len(sti) == 1:
29                continue
30
31            cnt = defaultdict(int)
32            for b_val in sti:
33                cnt[b_val] += 1
34
35            total_sum = 0
36            for count in cnt.values():
37                ans += total_sum * count
38                total_sum += count
39
40        for mts in mid_to_slope.values():
41            if len(mts) == 1:
42                continue
43
44            cnt = defaultdict(int)
45            for k_val in mts:
46                cnt[k_val] += 1
47
48            total_sum = 0
49            for count in cnt.values():
50                ans -= total_sum * count
51                total_sum += count
52
53        return ans