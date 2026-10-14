# Last updated: 10/14/2026, 7:42:51 PM
1class Solution:
2    def resilientSubarray(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4        prefix = [0]
5        nums = [num % k for num in nums]
6        for num in nums:
7            prefix.append((prefix[-1] + num) % k)
8
9        counter = defaultdict(int)
10        rems = {}
11        prev = nums[0]
12        left = 0
13        for i in range(1, n):
14            num = nums[i]
15
16            window = i - left
17            tot = (prefix[i] - prefix[left]) % k
18            if tot == prev:
19                counter[prev] = max(counter[prev], window)
20                
21            if num != prev:
22                left = i
23            prev = num
24
25        tot = (prefix[-1] - prefix[left]) % k
26        window = n - left
27        if tot == prev:
28            counter[prev] = max(counter[prev], window)
29
30        best = 1
31        for rem in range(k):
32            best = max(best, counter[rem])
33
34        return best