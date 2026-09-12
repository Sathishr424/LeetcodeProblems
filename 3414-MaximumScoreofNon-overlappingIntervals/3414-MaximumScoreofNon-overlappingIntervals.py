# Last updated: 9/12/2026, 10:05:35 AM
1class Solution:
2    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
3        n = len(intervals)
4        new_intervals = [(x, y, w, i) for i, (x, y, w) in enumerate(intervals)]
5        new_intervals.sort()
6        indexes = [x for x, _, _, _ in new_intervals]
7        # print(new_intervals)
8        # print(indexes)
9
10        def isSmallest(a1, a2):
11            for i in range(min(len(a1), len(a2))):
12                if a1[i] < a2[i]: return True
13                elif a2[i] < a1[i]: return False
14            
15            return len(a1) <= len(a2)
16
17        @cache
18        def rec(index, rem):
19            if index == n or rem == 0: return 0, []
20
21            w, arr = rec(index + 1, rem)
22            right = bisect_right(indexes, new_intervals[index][1], lo=index)
23            w2, arr2 = rec(right, rem - 1)
24            w2 += new_intervals[index][2]
25            arr2 = [new_intervals[index][3]] + arr2
26
27            if w > w2:
28                return w, arr
29            elif w2 > w:
30                return w2, arr2
31            elif isSmallest(sorted(arr), sorted(arr2)):
32                return w, arr
33            else:
34                return w2, arr2
35
36        w, ret = rec(0, 4)
37        rec.cache_clear()
38        return sorted(ret)