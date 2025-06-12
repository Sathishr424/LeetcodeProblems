# Last updated: 12/6/2025, 5:52:16 am
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while right-left > 1:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
            
        if nums[left] > nums[right]: return nums[right]

        return nums[left]