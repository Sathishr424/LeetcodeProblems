# Last updated: 24/9/2025, 9:36:15 pm
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        diff_arr = []
        n = len(nums1)
        for i in range(n):
            diff_arr.append(nums1[i] - nums2[i])

        # nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff
        # d[i] <= d[j] + diff
        
        ret = 0
        sl = SortedList()
        for i in range(n):
            num = diff_arr[i] + diff
            index = sl.bisect_right(num)
            ret += index
            sl.add(diff_arr[i])

        return ret

        