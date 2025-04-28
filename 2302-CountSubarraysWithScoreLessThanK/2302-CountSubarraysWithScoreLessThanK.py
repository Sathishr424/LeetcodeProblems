# Last updated: 28/4/2025, 4:21:17 pm
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        [2,1,4,3,5]
        """
        ret = 0
        left = 0
        cnt = 0
        s = 0
        prev = 0
        for i, num in enumerate(nums):
            cnt += 1
            s += num

            while s * cnt >= k and left <= i:
                cnt -= 1
                s -= nums[left]
                left += 1
                prev -= 1
            
            prev += 1
            ret += prev
        
        return ret