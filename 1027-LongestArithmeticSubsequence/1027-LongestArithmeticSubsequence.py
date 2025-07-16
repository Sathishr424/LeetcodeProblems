# Last updated: 16/7/2025, 6:54:17 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = max(nums)
        ret = 0
        m = maxi * 3 + 1
        counter = [[0] * m for _ in range(maxi * 2 + 1)]
        is_on_diff = [0] * (maxi * 2 + 1)

        for i in range(n):
            for j in range(i+1, n):
                is_on_diff[nums[j] - nums[i] + maxi] = 1
        
        for diff in range(-maxi, maxi + 1):
            index = diff + maxi
            if is_on_diff[index] == 0: continue
            for num in nums:
                counter[index][num + maxi] = counter[index][ (num - diff + maxi) ] + 1
            ret = cmax(ret, max(counter[index]))

        return ret

