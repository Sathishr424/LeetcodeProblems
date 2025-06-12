# Last updated: 12/6/2025, 5:35:33 am
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ret = 0

        for i in range(2, len(nums)):
            if nums[i-2] == 0:
                nums[i-2] ^= 1
                nums[i-1] ^= 1
                nums[i] ^= 1
                ret += 1
        # print(nums)
        return ret if sum(nums[i-2:]) == 3 else -1
