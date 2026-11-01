# Last updated: 11/1/2026, 9:51:48 PM
1class Solution:
2    def minOperations(self, nums: list[int], locked: list[int], k: int) -> int:
3        n = len(nums)
4
5        sorted_nums = sorted(nums)
6        op = 0
7        ans = 0
8        def bubbleSort(nums):
9            nonlocal op, ans
10            is_sorted = True
11            for i in range(n-1):
12                if nums[i] > nums[i + 1]:
13                    if locked[i] == 1:
14                        if op == k: return False, nums
15                        op += 1
16                        locked[i] = 0
17                    if locked[i + 1] == 1:
18                        if op == k: return False, nums
19                        op += 1
20                        locked[i + 1] = 0
21
22                    nums[i + 1], nums[i] = nums[i], nums[i + 1]
23                    ans += 1
24                    is_sorted = False
25            if is_sorted: return True, nums
26            return bubbleSort(nums)
27
28        is_sorted, nums = bubbleSort(nums)
29        if not is_sorted: return -1
30        return op + ans