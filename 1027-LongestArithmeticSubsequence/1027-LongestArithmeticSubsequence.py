# Last updated: 16/7/2025, 6:53:24 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = max(nums)
        ret = 0
        m = maxi * 3 + 1
        counter = [[0] * m for _ in range(maxi * 2 + 1)]
        for diff in range(-maxi, maxi + 1):
            index = diff + maxi
            for num in nums:
                counter[index][num + maxi] = counter[index][ (num - diff + maxi) ] + 1
            ret = cmax(ret, max(counter[index]))

        return ret

