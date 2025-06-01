# Last updated: 1/6/2025, 11:21:22 pm
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = 1
        r = len(nums)

        while l < r:
            mid = (l + r) // 2

            cnt = 0
            for num in nums:
                cnt += num <= mid
            
            if cnt > mid:
                r = mid
            else:
                l = mid + 1
        
        return l
