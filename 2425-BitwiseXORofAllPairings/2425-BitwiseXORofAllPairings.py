# Last updated: 24/9/2025, 9:36:06 pm
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        xor = 0
        for num in nums2:
            xor ^= num

        final = 0
        for i in range(n):
            if m % 2 == 0:
                final ^= xor
            else:
                final ^= xor ^ nums1[i]

        return final