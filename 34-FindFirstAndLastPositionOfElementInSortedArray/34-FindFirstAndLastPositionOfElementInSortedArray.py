# Last updated: 12/6/2025, 5:54:44 am
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]

        def bs(left, right):
            if left >= right: return left

            mid = (right+left) // 2

            if nums[mid] > target:
                return bs(left, mid-1)
            elif nums[mid] < target:
                return bs(mid+1, right)
            else:
                return bs(left, mid)

        def bs_right(left, right):
            if left >= right: return left

            mid = ceil((right+left) / 2)

            if nums[mid] > target:
                return bs_right(left, mid-1)
            else:
                return bs_right(mid, right)
        
        start = bs(0, len(nums)-1)
        if nums[start] != target: return [-1, -1]

        return [start, bs_right(start, len(nums)-1)]
