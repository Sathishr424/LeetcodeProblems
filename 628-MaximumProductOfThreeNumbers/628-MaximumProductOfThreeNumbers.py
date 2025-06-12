# Last updated: 12/6/2025, 5:48:02 am
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)

        def rec(arr, sum, cnt):
            nonlocal ans
            if cnt == 3:
                ans = max(ans, sum)
            for i in range(len(arr)):
                rec(arr[:i] + arr[i+1:], sum*arr[i], cnt+1)

        ans = -float('inf')
        if n <= 6:
            rec(nums, 1, 0)
            return ans

        nums.sort()

        rec(nums[:3]+nums[-3:], 1, 0)
        return ans