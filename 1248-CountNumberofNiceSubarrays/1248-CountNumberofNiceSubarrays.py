# Last updated: 26/4/2025, 2:35:06 am
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd = 0
        """
        [1,2,2,2,1,2,2,1,2,2,2]
        """
        prefix = [0] * (10 ** 5 + 1)
        prefix[0] = 1
        ret = 0

        for num in nums:
            odd += num % 2

            ret += prefix[odd-k]
            prefix[odd] += 1
        
        return ret

