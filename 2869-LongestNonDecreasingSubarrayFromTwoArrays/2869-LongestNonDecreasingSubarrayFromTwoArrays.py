# Last updated: 12/6/2025, 5:36:46 am
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        memo = {}
        def rec(index, prev=-1):
            if index == n: return 0
            if (index,prev) in memo: return memo[(index,prev)]
            # print(nums1[index], nums2[index], prev)
            memo[(index,prev)] = 0
            if nums1[index] >= prev:
                memo[(index,prev)] = rec(index+1, nums1[index]) + 1
            if nums2[index] >= prev:
                memo[(index,prev)] = max(memo[(index,prev)], rec(index+1, nums2[index]) + 1)

            return memo[(index,prev)]
            
        ans = max([rec(i) for i in range(n)])
        # print(memo)
        return ans
