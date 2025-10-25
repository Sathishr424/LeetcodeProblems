# Last updated: 25/10/2025, 8:32:52 pm
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        diff = []
        for i in range(n):
            diff.append(nums1[i] - nums2[i])

        extra = nums2[n]
        op = 1
        min_extra = inf

        for i in range(n):
            need = diff[i]
            x = nums1[i]
            y = nums2[i]

            op += abs(need)

            if y < x:
                y, x = x, y

            if extra >= x and extra <= y:
                min_extra = 0
            else:
                min_extra = min(min_extra, min(abs(x - extra), abs(y - extra)))

        return op + min_extra
            
        