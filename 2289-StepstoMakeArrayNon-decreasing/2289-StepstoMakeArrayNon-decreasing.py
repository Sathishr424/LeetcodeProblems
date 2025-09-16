# Last updated: 16/9/2025, 6:59:55 am
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)

        stack = []
        dp = [0] * n
        max_cnt = 0
        for i in range(n-1, -1, -1):
            # cnt = 0
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                dp[i] = max(dp[index], dp[i] + 1)
            
            stack.append(i)
            max_cnt = max(max_cnt, dp[i])
        
        # print(stack)
        # print(dp)
        return max_cnt
            