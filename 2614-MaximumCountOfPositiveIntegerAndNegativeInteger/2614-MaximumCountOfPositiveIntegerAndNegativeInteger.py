# Last updated: 12/6/2025, 5:37:31 am
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        def bs_left(l, r):
            while l < r:
                mid = (l+r) //  2

                if nums[mid] < 0:
                    l = mid+1
                else:
                    r = mid
            return l
        
        def bs_right(l, r):
            while l < r:
                mid = ceil((l+r) /  2)

                if nums[mid] > 0:
                    r = mid-1
                else:
                    l = mid
            return l
        
        l = bs_left(0, n-1)
        r = bs_right(l, n-1)
        
        # print(l, r, nums[l], nums[r], l, n-r-(nums[r] == 0))

        return max(l+(nums[l] < 0), n-r-(nums[r] == 0))