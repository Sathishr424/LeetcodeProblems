# Last updated: 14/4/2025, 5:28:30 pm
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start = 0
        end = n-1

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                for j in range(n-1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        start = i+1
                        break
                break
        
        for k in range(start, (start+end)//2 + 1):
            nums[k], nums[end] = nums[end], nums[k]
            end -= 1    