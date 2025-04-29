# Last updated: 29/4/2025, 11:11:34 am
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ret = 0
        maxi = max(nums)

        cnt = 0
        left = 0
        prev = 0
        
        for i, num in enumerate(nums):
            cnt += num == maxi

            while cnt == k:
                cnt -= nums[left] == maxi
                left += 1
            
            ret += left
        
        return ret