# Last updated: 8/29/2026, 4:34:17 PM
1class Solution:
2    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
3        n = len(nums)
4
5        sorted_nums = []
6        for i, num in enumerate(nums):
7            sorted_nums.append((num, i))
8        sorted_nums.sort()
9
10        group_relation = [i for i in range(n)]
11        groups = defaultdict(list)
12        group_id = 0
13        prev = -limit
14        for num, i in sorted_nums:
15            if num - prev > limit:
16                group_id += 1
17
18            groups[group_id].append(num)
19            group_relation[i] = group_id
20            prev = num
21
22        for group in groups:
23            groups[group].sort(reverse=True)
24
25        ret = []
26        for i in range(n):
27            ret.append(groups[group_relation[i]].pop())
28
29        return ret