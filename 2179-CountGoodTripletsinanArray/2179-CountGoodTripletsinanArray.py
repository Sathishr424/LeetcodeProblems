# Last updated: 25/8/2025, 10:03:01 pm
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        ret = 0

        indexes = [0] * n
        for i in range(n):
            indexes[nums1[i]] = i

        from_left = [0] * n
        sl = SortedList()
        for i in range(n):
            sl.add(indexes[nums2[i]])
            from_left[i] = sl.bisect_left(indexes[nums2[i]])
        
        sl = SortedList()
        for i in range(n-1, -1, -1):
            sl.add(indexes[nums2[i]])

            cnt = len(sl) - sl.bisect_left(indexes[nums2[i]]) - 1
            ret += from_left[i] * cnt

        return ret