# Last updated: 11/10/2025, 8:12:28 pm
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        diff = [0, 0]
        for i in range(1, n):
            diff.append(nums[i-1] + nums[i])

        @cache
        def rec(index):
            if index == n: return 0

            if diff[index] == nums[index]:
                return rec(index + 1) + 1
            else:
                return 0

        ans = 2
        for i in range(2, n):
            ans = max(ans, rec(i) + 2)
            
        rec.cache_clear()
        return ans