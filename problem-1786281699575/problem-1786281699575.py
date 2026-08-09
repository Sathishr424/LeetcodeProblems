# Last updated: 8/9/2026, 6:51:39 PM
1class Solution:
2    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
3        n = len(nums)
4        mod = 10**9 + 7
5
6        for i, num in enumerate(nums):
7            if num < a:
8                nums[i] = 0
9            elif num > b:
10                nums[i] = 2
11            else:
12                nums[i] = 1
13
14        arr = SortedList()
15        ans = 0
16        for i in range(n-1, -1, -1):
17            ans += arr.bisect_left(nums[i])
18            arr.add(nums[i])
19
20        return ans % mod