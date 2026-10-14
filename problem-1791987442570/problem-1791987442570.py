# Last updated: 10/14/2026, 7:47:22 PM
1class Solution:
2    def resilientSubarray(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4        prefix = [0]
5        nums = [num % k for num in nums]
6        for num in nums:
7            prefix.append((prefix[-1] + num) % k)
8
9        best = 1
10        prev = nums[0]
11        left = 0
12        for i in range(1, n):
13            num = nums[i]
14
15            window = i - left
16            tot = (prefix[i] - prefix[left]) % k
17            if tot == prev:
18                best = max(best, window)
19                
20            if num != prev:
21                left = i
22            prev = num
23
24        tot = (prefix[-1] - prefix[left]) % k
25        window = n - left
26        if tot == prev:
27            best = max(best, window)
28
29        return best