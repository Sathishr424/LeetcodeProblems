# Last updated: 10/10/2025, 1:08:08 am
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        l = 0
        r = 0
        while l < m and r < n:
            while l < m and nums1[l] < nums2[r]:
                l += 1
            if l == m: return -1
            while r < n and nums2[r] < nums1[l]:
                r += 1
            if r == n: return -1
            
            if nums1[l] == nums2[r]: return nums1[l]
            l += 1

        return -1