# Last updated: 6/4/2025, 9:47:02 pm
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)

        dp = defaultdict(list)
        ret = []
        nums.sort()

        for i in range(n-1, -1, -1):
            num = nums[i]
            dp[num] = [num]
            for j in range(i+1, n):
                if nums[j] % num  == 0:
                    if len(dp[nums[j]])+1 > len(dp[num]):
                        dp[num] = [num] + dp[nums[j]]
            if len(dp[num]) > len(ret):
                ret = dp[num]

        return ret

