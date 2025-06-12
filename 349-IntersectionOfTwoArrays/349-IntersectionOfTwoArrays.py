# Last updated: 12/6/2025, 5:50:15 am
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = {}

        for num in nums1:
            hash[num] = 1
        
        tmp = {}
        ret = []
        
        for num in nums2:
            if num in hash and num not in tmp:
                ret.append(num)
                tmp[num] = 1
        
        return ret
