# Last updated: 16/7/2025, 6:54:35 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        maxi = max(nums)
        ret = 0

        for diff in range(-maxi, maxi + 1):
            counter = [0] * (maxi * 3 + 1)
            for num in nums:
                counter[num + maxi] = counter[ (num - diff + maxi) ] + 1
            ret = cmax(ret, max(counter))

        return ret

