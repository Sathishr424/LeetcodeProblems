# Last updated: 1/6/2025, 11:15:20 pm
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        l = 1
        r = n

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
