# Last updated: 29/6/2025, 7:11:06 am
N = 10 ** 5 + 1
fact = [0] * N
fact[1] = 1
mod = 10 ** 9 + 7
s = 1
for i in range(2, N):
    fact[i] = (s + 1) % mod
    s = (s + fact[i]) % mod

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # 2 3 5 6 7
        # 16 8 4 2 1
        # (3) (3 5) (3 6) (3 7) (3 5 6) (3 5 6 7) (3 5 7) (3 6 7)

        nums.sort()
        ret = 0

        for i in range(n):
            index = bisect_right(nums, target - nums[i])
            if index >= i:
                ret = (ret + fact[index - i]) % mod
        return ret

