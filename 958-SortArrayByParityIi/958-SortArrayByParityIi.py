# Last updated: 12/6/2025, 5:45:17 am
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)

        even = 0
        odd = 1

        while even < n and odd < n:
            if nums[even] % 2 != 0 and nums[odd] % 2 == 0:
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
                odd += 2
            else:
                if nums[odd] % 2 != 0:
                    odd += 2
                if nums[even] % 2 == 0:
                    even += 2
        
        return nums
