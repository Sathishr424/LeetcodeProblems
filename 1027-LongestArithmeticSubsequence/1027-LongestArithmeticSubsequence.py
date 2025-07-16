# Last updated: 16/7/2025, 6:43:23 pm
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        maxi = max(nums)
        ret = 0

        for diff in range(-maxi, maxi + 1):
            counter = [0] * (maxi * 3 + 1)
            for num in nums:
                counter[num + maxi] = counter[ (num - diff + maxi) ] + 1
                ret = max(ret, counter[num + maxi])

        return ret

