# Last updated: 10/5/2025, 12:36:56 pm
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum_1 = 0
        sum_2 = 0
        z1 = 0
        z2 = 0

        for num in nums1:
            if num == 0:
                z1 += 1
            else:
                sum_1 += num

        for num in nums2:
            if num == 0:
                z2 += 1
            else:
                sum_2 += num

        sum_1 += z1
        sum_2 += z2

        if sum_1 == sum_2: return sum_1
        elif sum_1 > sum_2 and z2: return sum_1
        elif sum_2 > sum_1 and z1: return sum_2
        return -1


