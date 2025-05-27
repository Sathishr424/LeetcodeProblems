# Last updated: 28/5/2025, 3:23:05 am
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1: return nums
        # 1, 2, 3, 4, 5
        # 1, 2, 3, 5, 4

        # 1, 3, 4, 5, 2
        # 1, 3, 2, 4, 5

        # 1, 4, 2, 3, 5
        # 1, 4, 2, 5, 3 => 3, 2, 5
        # 1, 4, 3, 2, 5
        # 1, 4, 3, 5, 2
        # 1, 4, 5, 2, 3
        # 1, 4, 5, 3, 2 => 5, 4, 3, 2
        # 1, 5, 2, 3, 4

        # 3, 6, 5, 4, 2, 1

        # 1, 5, 4, 3, 2

        n = len(nums)
        index = 0
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                for j in range(n-1, -1, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                index = i+1
                break
        
        left = index
        right = n-1
        for i in range((right-left+1)//2):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
