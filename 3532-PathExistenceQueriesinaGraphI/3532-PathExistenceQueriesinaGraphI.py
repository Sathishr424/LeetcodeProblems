# Last updated: 7/11/2026, 2:18:01 AM
1class Solution:
2    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
3        indexes = [-1]
4        for i in range(1, n):
5            if nums[i] - nums[i - 1] > maxDiff:
6                indexes.append(i)
7        indexes.append(n)
8        # print(indexes)
9
10        m = len(indexes) - 1
11        ret = []
12        for u, v in queries:
13            left = bisect_right(indexes, u)
14            right = bisect_right(indexes, v)
15            # print((u, v), (left, right))
16            ret.append(left == right)
17
18        return ret