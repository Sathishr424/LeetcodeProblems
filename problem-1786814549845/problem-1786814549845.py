# Last updated: 8/15/2026, 10:52:29 PM
1class Solution:
2    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
3        n = len(series1)
4        m = len(series2)
5
6        i = 0
7        j = 0
8
9        ans = []
10        while i < n and j < m:
11            added = series2[j][1] + series1[i][1]
12            if series1[i][0] > series2[j][0]:
13                ans.append([series2[j][0], added])
14                j += 1
15            elif series1[i][0] < series2[j][0]:
16                ans.append([series1[i][0], added])
17                i += 1
18            else:
19                ans.append([series1[i][0], added])
20                i += 1
21                j += 1
22
23        while i < n:
24            ans.append(series1[i])
25            i += 1
26
27        while j < m:
28            ans.append(series2[j])
29            j += 1
30
31        return ans