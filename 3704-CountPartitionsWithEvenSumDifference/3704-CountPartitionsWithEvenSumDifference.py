# Last updated: 12/6/2025, 5:35:03 am
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        curr = 0
        res = 0
        
        for i in range(len(nums)-1):
            curr += nums[i]
            total -= nums[i]

            # print(nums[:i+1], nums[i+1:], curr, total)

            if (curr - total) % 2 == 0: res += 1

        return res