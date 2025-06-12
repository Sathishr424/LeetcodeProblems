# Last updated: 12/6/2025, 5:37:09 am
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        l = 0
        r = 0

        m = len(nums1)
        n = len(nums2)
        ret = []
        while l < m and r < n:
            if nums1[l][0] > nums2[r][0]:
                ret.append(nums2[r])
                r += 1
            elif nums1[l][0] < nums2[r][0]:
                ret.append(nums1[l])
                l += 1
            else:
                ret.append([nums1[l][0], nums1[l][1] + nums2[r][1]])
                l += 1
                r += 1
        
        while l < m:
            ret.append(nums1[l])
            l += 1

        while r < n:
            ret.append(nums2[r])
            r += 1
        
        return ret
