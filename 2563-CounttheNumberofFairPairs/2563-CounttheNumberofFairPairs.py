# Last updated: 19/4/2025, 3:22:37 pm
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        ret = 0

        def binary_search(nums, val, l):
            r = len(nums)

            while l < r:
                mid = (l+r) // 2

                if nums[mid] >= val:
                    r = mid
                else:
                    l = mid+1
            
            return l

        for i in range(n):
            l = lower - nums[i]
            r = upper - nums[i]

            ret += binary_search(nums, r+1, i+1)-binary_search(nums, l, i+1)
        
        return ret




