# Last updated: 11/1/2026, 9:58:49 PM
1class Solution:
2    def minOperations(self, nums: list[int], locked: list[int], k: int) -> int:
3        n = len(nums)
4
5        op = 0
6        ans = 0
7        def bubbleSort(nums):
8            nonlocal op, ans
9            is_sorted = True
10            for i in range(n-1):
11                if nums[i] > nums[i + 1]:
12                    if locked[i] == 1:
13                        if op == k: return False, nums
14                        op += 1
15                        locked[i] = 0
16                    if locked[i + 1] == 1:
17                        if op == k: return False, nums
18                        op += 1
19                        locked[i + 1] = 0
20
21                    nums[i + 1], nums[i] = nums[i], nums[i + 1]
22                    ans += 1
23                    is_sorted = False
24            if is_sorted: return True, nums
25            return bubbleSort(nums)
26
27        is_sorted, nums = bubbleSort(nums)
28        if not is_sorted: return -1
29        return op + ans