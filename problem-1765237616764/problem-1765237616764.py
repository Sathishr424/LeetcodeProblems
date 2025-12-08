# Last updated: 12/9/2025, 5:16:56 AM
1class Solution:
2    def beautifulSubsets(self, nums: List[int], k: int) -> int:
3        n = len(nums)
4        nums.sort()
5        there = defaultdict(list)
6        for i in range(n):
7            there[nums[i]].append(i)
8        # print(nums, dict(there))
9        uniq = set()
10        full_mask = (1 << n) - 1
11
12        def rec(index, mask):
13            if index == n:
14                if mask != full_mask: uniq.add(mask)
15                return
16            if mask & (1 << index): return rec(index + 1, mask)
17            
18            rec(index + 1, mask | (1 << index))
19            if len(there[nums[index] + k]):
20                # print(format(mask, '05b'), nums[index])
21                new_mask = mask
22                for i in there[nums[index] + k]:
23                    new_mask |= 1 << i
24                rec(index + 1, new_mask)
25            else:
26                rec(index + 1, mask)
27
28        rec(0, 0)
29        # for u in uniq:
30        #     print(format(u, '05b'))
31        return len(uniq)