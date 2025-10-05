# Last updated: 5/10/2025, 9:02:03 am
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        xor = 0
        for num in nums:
            xor ^= num
        if xor > 0:
            return n
        # print(xor)
        # [print(format(num, '05b')) for num in nums]
        best = 0
        for i in range(32):
            cnt = 0
            xor = 0
            for num in nums:
                if num & (1 << i):
                    cnt += 1
                else:
                    xor ^= num

            if cnt % 2 == 0:
                best = max(best, cnt - 1)
                if cnt > 1 or xor > 0:
                    best = max(best, n - 1)
            else:
                best = max(best, n)

        return best
        