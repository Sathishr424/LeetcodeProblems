# Last updated: 12/6/2025, 5:53:45 am
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l = 0
        r = n-1
        while l<r:
            mid = (r+l)//2
            if nums[r] == nums[l]:
                l += 1
            elif nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] <= nums[r]:
                r = mid
            else: break
        mid = l

        if target > nums[-1]:
            l = 0
            r = mid-1
        elif target < nums[-1]:
            l = mid
            r = n-1
        else: return True

        while l<=r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else: return True
        return False