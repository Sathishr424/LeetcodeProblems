# Last updated: 29/6/2025, 6:58:04 am
def c_fact(n):
    if n == 1: return 1
    return c_fact(n - 1) + 1

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)

        # 2 3 5 6 7
        # 16 8 4 2 1
        # (3) (3 5) (3 6) (3 7) (3 5 6) (3 5 6 7) (3 5 7) (3 6 7)

        nums.sort()
        # print(nums)
        ret = 0

        for i in range(n):
            index = bisect_right(nums, target - nums[i])
            # print(i, index, (index - i))
            if index >= i:
                # print((1 << (index - i)) // 2)
                ret += (1 << (index - i)) // 2
                ret %= mod
        
        return ret

