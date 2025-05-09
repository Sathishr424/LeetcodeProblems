# Last updated: 9/5/2025, 3:40:58 pm
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] + [-1 for _ in range(target)]
        current_max_sum = 0
        for num in nums:
            if num > target:
                break
            current_max_sum = min(num + current_max_sum, target)
            for current_target in range(current_max_sum, num - 1, -1):
                if dp[current_target - num] + 1 > dp[current_target]:
                    dp[current_target] = dp[current_target - num] + 1
        return dp[target] if dp[target] > 0 else -1