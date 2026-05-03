# Last updated: 5/3/2026, 5:21:22 PM
1class Solution:
2    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
3        n = len(nums)
4
5        prefix = [0]
6        for num in nums:
7            prefix.append(prefix[-1] + (num % 2 == 0))
8        ans = []
9
10        for left, right, k in queries:
11            l = k
12            r = k + (right - left + 1)
13
14            while l < r:
15                mid = (l + r) // 2
16                val = mid * 2
17
18                need = mid - k
19
20                index = bisect_right(nums, val, lo=left, hi=right + 1)
21                evens = prefix[index] - prefix[left]
22                # print(l, mid, r, (left, right, k), (val, need, evens), index)
23
24                if evens > need:
25                    l = mid + 1
26                else:
27                    r = mid
28
29            ans.append(l * 2)
30
31        return ans