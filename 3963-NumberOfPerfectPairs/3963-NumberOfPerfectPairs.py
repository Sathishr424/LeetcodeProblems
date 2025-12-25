# Last updated: 12/25/2025, 7:09:51 PM
class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0
        for i in range(n):
            nums[i] = abs(nums[i])
        nums.sort()
        # print(nums)

        for i in range(n):
            index = bisect_right(nums, abs(nums[i] + nums[i]))
            # print(i, nums[i], index)
            index -= 1
            pair = index - i
            ret += max(0, pair)

        return ret

            
            