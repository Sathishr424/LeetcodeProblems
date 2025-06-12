# Last updated: 12/6/2025, 5:42:45 am
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

