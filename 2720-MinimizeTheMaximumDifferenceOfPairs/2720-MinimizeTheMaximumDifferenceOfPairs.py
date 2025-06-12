# Last updated: 12/6/2025, 5:37:07 am
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0: return 0
        nums.sort()
        n = len(nums)
        def countPairs(diff):
            i = 0
            cnt = 0
            while i < n-1:
                if nums[i+1] - nums[i] <= diff:
                    cnt += 1
                    i += 1
                i += 1
            return cnt
        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            mid = left + ((right - left)//2)
            if countPairs(mid) >= p:
                right = mid
            else:
                left = mid + 1
        return left