# Last updated: 8/29/2026, 4:33:04 PM
1class Solution:
2    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
3        n = len(nums)
4
5        sorted_nums = []
6        for i, num in enumerate(nums):
7            sorted_nums.append((num, i))
8
9        sorted_nums.sort()
10
11        group_relation = [i for i in range(n)]
12        groups = defaultdict(list)
13        group_id = 0
14        prev = -10**20
15        for num, i in sorted_nums:
16            if num - prev > limit:
17                group_id += 1
18
19            groups[group_id].append(num)
20            group_relation[i] = group_id
21            prev = num
22
23        for group in groups:
24            groups[group].sort(reverse=True)
25
26        ret = []
27        for i in range(n):
28            ret.append(groups[group_relation[i]].pop())
29
30        return ret