# Last updated: 26/10/2025, 2:01:32 pm
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)

        nums.sort(key=lambda x: abs(x))
        ans = 0
        left = nums[:n//2]
        right = nums[n//2:]

        for num in right:
            ans += pow(num, 2)

        for num in left:
            ans -= pow(num, 2)

        return ans