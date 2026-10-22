# Last updated: 10/22/2026, 4:31:43 PM
1class Solution:
2    def minOperations(self, nums: List[int]) -> int:
3        # [1, 0, 3, 4, 2]
4        # [4, 2, 3, 5] [5, 3, 2, 4]
5        # [2, 3, 5, 4]
6        # [3, 5, 4, 2]
7        # [5, 4, 2, 3]
8        # [4, 2, 3, 5]
9
10        # [0, 2, 1] => [0, 1, 2]
11        # [1, 0, 2] => [1, 2, 0]
12        # [2, 0, 1, 3] => [2, 3, 3, 0]
13
14        n = len(nums)
15        def do(nums):
16            arr = [0] * n
17            for i in range(n):
18                index = nums[i]
19                to_add = (i - index) % n
20                arr[i] = to_add
21    
22            return arr
23        arr = do(nums)
24        arr2 = do(nums[::-1])
25
26        a1 = arr.count(arr[0]) == n
27        a2 = arr2.count(arr2[0]) == n
28        if not a1 and not a2: return -1
29        # print(a1, a2)
30        # print(arr)
31        # print(arr2)
32        best = inf
33        if a1:
34            best = min(arr[0], n - arr2[-1] + 1)
35        elif a2:
36            best = min(arr2[1] + 1, n - arr[-1])
37        return best