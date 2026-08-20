# Last updated: 8/20/2026, 12:15:40 PM
1class Solution:
2    def resultArray(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4
5        arr1 = [nums[0]]
6        arr2 = [nums[1]]
7
8        for i in range(2, n):
9            if arr1[-1] > arr2[-1]:
10                arr1.append(nums[i])
11            else:
12                arr2.append(nums[i])
13
14        return arr1 + arr2