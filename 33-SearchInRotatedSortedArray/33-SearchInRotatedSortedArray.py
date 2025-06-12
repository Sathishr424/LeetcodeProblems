# Last updated: 12/6/2025, 5:54:46 am
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findRotateIndex(left, right):
            if left >= right: return left
            mid = (left+right) // 2

            if nums[mid] <= nums[right]:
                return findRotateIndex(left, mid)
            elif nums[mid] > nums[right]:
                return findRotateIndex(mid+1, right)
        
        index = findRotateIndex(0, len(nums)-1)

        l = 0
        r = index-1
        if nums[index] == target: return index
        elif target <= nums[-1]:
            l = index
            r = len(nums)-1
        
        while l <= r:
            mid = (l+r) // 2

            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                return mid
        
        return -1

