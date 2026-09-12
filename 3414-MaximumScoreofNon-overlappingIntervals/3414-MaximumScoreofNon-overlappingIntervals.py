# Last updated: 9/12/2026, 10:06:32 AM
1class Solution:
2    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
3        n = len(intervals)
4        new_intervals = [(x, y, w, i) for i, (x, y, w) in enumerate(intervals)]
5        new_intervals.sort()
6        indexes = [x for x, _, _, _ in new_intervals]
7
8        def isSmallest(a1, a2):
9            for i in range(min(len(a1), len(a2))):
10                if a1[i] < a2[i]: return True
11                elif a2[i] < a1[i]: return False
12            
13            return len(a1) <= len(a2)
14
15        @cache
16        def rec(index, rem):
17            if index == n or rem == 0: return 0, []
18
19            w, arr = rec(index + 1, rem)
20            right = bisect_right(indexes, new_intervals[index][1], lo=index)
21            w2, arr2 = rec(right, rem - 1)
22            w2 += new_intervals[index][2]
23            arr2 = sorted([new_intervals[index][3]] + arr2)
24
25            if w > w2:
26                return w, arr
27            elif w2 > w:
28                return w2, arr2
29            elif isSmallest(arr, arr2):
30                return w, arr
31            else:
32                return w2, arr2
33
34        _, ret = rec(0, 4)
35        rec.cache_clear()
36        return ret