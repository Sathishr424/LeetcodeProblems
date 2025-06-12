# Last updated: 12/6/2025, 5:55:42 am
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        tot = m+n
        mid = tot // 2

        l = 0
        r = 0

        prev = None
        cnt = -1

        def getMedian(left, right):
            if tot % 2 == 0: return (left+right) / 2
            return right

        while l < m and r < n:
            tmp = prev
            if nums1[l] < nums2[r]:
                prev = nums1[l]
                l += 1
            else:
                prev = nums2[r]
                r += 1
            cnt += 1

            if cnt == mid:
                return getMedian(tmp, prev)
        
        while l < m:
            tmp = prev
            prev = nums1[l]
            cnt += 1
            l += 1

            if cnt == mid:
                return getMedian(tmp, prev)
            
        while r < n:
            tmp = prev
            prev = nums2[r]
            cnt += 1
            r += 1
            
            if cnt == mid:
                return getMedian(tmp, prev)

        return 0


