# Last updated: 12/6/2025, 5:48:56 am
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        hash = {}

        for i in range(len(nums1)):
            hash[nums1[i]] = i
            ret.append(-1)
        
        arr = []
        for i in range(len(nums2)-1, -1, -1):
            while arr and arr[-1] < nums2[i]:
                arr.pop()
            
            if arr and nums2[i] in hash:
                ret[hash[nums2[i]]] = arr[-1]
            
            arr.append(nums2[i])

        return ret
        
