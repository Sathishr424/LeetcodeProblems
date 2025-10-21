# Last updated: 21/10/2025, 1:33:51 pm
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        nums.sort()

        cnts = [0] * n
        cnt = 1
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 1
            cnts[i-cnt+1] = cnt

        best = 1
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]: continue

            left = bisect_left(nums, nums[i] - k)
            right = bisect_right(nums, nums[i] + k)

            best = max(best, min(right - left, numOperations + cnts[i]))
        
        for i in range(n):
            left = bisect_left(nums, nums[i] - (k * 2))
            right = bisect_right(nums, nums[i] + (k * 2))

            best = max( best, min(numOperations, i - left + 1), min(numOperations, right - i) )
        
        return best