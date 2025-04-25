# Last updated: 26/4/2025, 2:58:45 am
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 0
        maxi = max(nums)
        cnt = 0
        left = 0

        for i, num in enumerate(nums):
            cnt += num == maxi

            while cnt == k and left <= i:
                cnt -= nums[left] == maxi
                left += 1
            
            ret += left
        
        return ret