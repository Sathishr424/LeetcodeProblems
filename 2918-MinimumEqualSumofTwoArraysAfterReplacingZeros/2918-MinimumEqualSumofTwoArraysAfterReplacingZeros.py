# Last updated: 10/5/2025, 12:26:08 pm
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        m = len(nums1)

        sum_1 = sum(nums1)
        sum_2 = sum(nums2)
        
        zero_1 = False
        for num in nums1:
            if num == 0:
                sum_1 += 1
                zero_1 = True
        
        zero_2 = False
        for num in nums2:
            if num == 0:
                sum_2 += 1
                zero_2 = True
        
        if sum_1 == sum_2: return sum_1
        elif sum_1 > sum_2:
            if zero_2: return sum_1
            return -1
        else:
            if zero_1: return sum_2
            return -1


