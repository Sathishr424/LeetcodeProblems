# Last updated: 10/14/2026, 7:42:21 PM
1class Solution:
2    def resilientSubarray(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4        prefix = [0]
5        nums = [num % k for num in nums]
6        for num in nums:
7            prefix.append((prefix[-1] + num) % k)
8
9        print(nums)
10        counter = defaultdict(int)
11        rems = {}
12        prev = nums[0]
13        left = 0
14        for i in range(1, n):
15            num = nums[i]
16
17            window = i - left
18            tot = (prefix[i] - prefix[left]) % k
19            if tot == prev:
20                counter[prev] = max(counter[prev], window)
21                
22            if num != prev:
23                left = i
24            prev = num
25
26        tot = (prefix[-1] - prefix[left]) % k
27        window = n - left
28        if tot == prev:
29            counter[prev] = max(counter[prev], window)
30        # print(dict(counter))
31
32        best = 1
33        for rem in range(k):
34            best = max(best, counter[rem])
35
36        return best