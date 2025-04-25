# Last updated: 26/4/2025, 2:22:11 am
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd = 0

        """
        [1,2,2,2,1,2,2,1,2,2,2]
        """
        prev = 0
        left = 0
        ret = 0
        for i, num in enumerate(nums):
            odd += num % 2

            if odd == k:
                prev = 0
                while left <= i and odd == k:
                    prev += 1
                    odd -= nums[left] % 2
                    left += 1
            
            ret += prev

        return ret