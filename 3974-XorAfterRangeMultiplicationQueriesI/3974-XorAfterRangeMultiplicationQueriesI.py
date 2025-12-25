# Last updated: 12/25/2025, 7:09:38 PM
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)

        for l, r, k, v in queries:
            i = l
            while i <= r:
                nums[i] = nums[i] * v % mod
                i += k

        ret = 0
        for num in nums:
            ret ^= num

        return ret
                