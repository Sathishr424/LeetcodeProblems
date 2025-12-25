# Last updated: 12/25/2025, 7:08:16 PM
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        increasing = [1] * n
        cnt = 1
        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                cnt += 1
            else:
                cnt = 1
            increasing[i] = cnt
        
        increasing_r = [1] * n
        cnt = 1
        for i in range(n-2, -1, -1):
            if nums[i + 1] >= nums[i]:
                cnt += 1
            else:
                cnt = 1
            increasing_r[i] = cnt
        
        # print(increasing)
        # print(increasing_r)
        ans = 1
        if n > 1: ans = 2
        ans = max(ans, max(increasing), max(increasing_r))
        for i in range(1, n-1):
            left = nums[i-1]
            right = nums[i + 1]
            l = increasing[i-1]
            r = increasing_r[i+1]

            if right >= left:
                ans = max(ans, l + r + 1)
            else:
                ans = max(ans, l + 1, r + 1)
        
        for i in range(n-1):
            ans = max(ans, increasing[i] + 1)
        
        for i in range(n-1, 0, -1):
            ans = max(ans, increasing_r[i] + 1)
        
        return ans
        