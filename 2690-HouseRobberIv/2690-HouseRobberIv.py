# Last updated: 12/6/2025, 5:37:16 am
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)

        left = min(nums)
        right = max(nums)

        while left < right:
            mid = (left+right) // 2

            cnt = 0
            i = 0

            while i < n:
                if nums[i] <= mid:
                    cnt += 1
                    i += 1
                i += 1
            
            if cnt >= k:
                right = mid
            else:
                left = mid+1
        
        return left



            