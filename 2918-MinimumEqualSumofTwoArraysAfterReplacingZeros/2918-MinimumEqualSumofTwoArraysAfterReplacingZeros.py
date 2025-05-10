# Last updated: 10/5/2025, 12:30:33 pm
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum_1 = sum(nums1)
        sum_2 = sum(nums2)
        
        sum_old_1 = sum_1
        sum_old_2 = sum_2

        for num in nums1:
            if num == 0:
                sum_1 += 1
        
        for num in nums2:
            if num == 0:
                sum_2 += 1
        
        if sum_1 == sum_2: return sum_1
        elif sum_1 > sum_2 and sum_old_2 != sum_2: return sum_1
        elif sum_2 > sum_1 and sum_old_1 != sum_1: return sum_2
        return -1


