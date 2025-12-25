# Last updated: 12/25/2025, 7:08:22 PM

class Solution:
    def maxSumOfSquares(self, n: int, sum: int) -> str:
        maxi = 9 * n
        rem = maxi-sum
        nums = [9] * n
        if rem < 0: return ''
        # print(nums, rem)
        for i in range(n-1, -1, -1):
            if rem == 0: break
            if rem >= 9:
                nums[i] -= 9
                rem -= 9
            else:
                nums[i] -= rem
                rem = 0

        ret = ''.join([str(num) for num in nums])
        if ret[0] == '0': return ''
        return ret