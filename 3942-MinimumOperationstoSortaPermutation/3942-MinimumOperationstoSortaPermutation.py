# Last updated: 10/22/2026, 4:34:27 PM
1class Solution:
2    def minOperations(self, nums: List[int]) -> int:
3        n = len(nums)
4        def do(nums):
5            arr = [0] * n
6            for i in range(n):
7                index = nums[i]
8                to_add = (i - index) % n
9                arr[i] = to_add
10            return arr
11
12        arr = do(nums)
13        arr2 = do(nums[::-1])
14
15        a1 = arr.count(arr[0]) == n
16        a2 = arr2.count(arr2[0]) == n
17        if not a1 and not a2: return -1
18        
19        best = inf
20        if a1:
21            best = min(arr[0], n - arr2[-1] + 1)
22        elif a2:
23            best = min(arr2[1] + 1, n - arr[-1])
24        return best