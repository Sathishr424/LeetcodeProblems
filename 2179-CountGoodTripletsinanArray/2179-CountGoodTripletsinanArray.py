# Last updated: 16/4/2025, 2:52:03 am
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        relation = [0] * n

        for i, num in enumerate(nums2):
            relation[num] = i
        
        arr = []
        left = SortedList()
        for num in nums1:
            arr.append(relation[num])
            left.add(relation[num])

        right = SortedList()
        ret = 0
        for num in arr[::-1]:
            left_index = bisect_left(left, num)
            right_index = bisect_left(right, num)

            ret += left_index * (len(right) - right_index)
            right.add(num)
            left.remove(num)
        
        return ret