# Last updated: 16/7/2025, 6:50:25 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = max(nums)
        ret = 0

        is_on_diff = [0] * (maxi * 2 + 1)

        for i in range(n):
            for j in range(i+1, n):
                is_on_diff[nums[j] - nums[i] + maxi] = 1

        for diff in range(-maxi, maxi + 1):
            if is_on_diff[diff + maxi] == 0: continue
            counter = [0] * (maxi * 3 + 1)
            for num in nums:
                counter[num + maxi] = counter[ (num - diff + maxi) ] + 1
            ret = cmax(ret, max(counter))

        return ret

