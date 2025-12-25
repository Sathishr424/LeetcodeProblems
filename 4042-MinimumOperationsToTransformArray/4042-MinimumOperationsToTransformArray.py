# Last updated: 12/25/2025, 7:08:54 PM
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        op = 1
        for i in range(n):
            op += abs(nums1[i] - nums2[i])

        extra = nums2[n]
        min_extra = inf

        for i in range(n):
            x = nums1[i]
            y = nums2[i]

            if y < x:
                y, x = x, y

            if extra >= x and extra <= y:
                min_extra = 0
            else:
                min_extra = min(min_extra, min(abs(x - extra), abs(y - extra)))

        return op + min_extra
            
        