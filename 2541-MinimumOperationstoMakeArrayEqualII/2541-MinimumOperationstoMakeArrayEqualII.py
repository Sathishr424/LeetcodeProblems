# Last updated: 10/10/2025, 3:13:20 am
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            if nums1 == nums2: return 0
            return -1
        n = len(nums1)

        diff = 0
        op = 0
        for i in range(n):
            d = nums2[i] - nums1[i]
            if d % k != 0: return -1
            if d > 0: op += d // k
            diff += d // k

        if diff == 0: return op
        return -1