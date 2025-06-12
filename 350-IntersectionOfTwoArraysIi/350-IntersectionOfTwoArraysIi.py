# Last updated: 12/6/2025, 5:50:14 am
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = {}
        for num in nums1:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
            
        ret = []

        for num in nums2:
            if num in hash and hash[num] >= 1:
                hash[num] -= 1
                ret.append(num)
        return ret