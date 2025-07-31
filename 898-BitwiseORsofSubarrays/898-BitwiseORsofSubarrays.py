# Last updated: 31/7/2025, 1:43:02 pm
class Solution:
    def subarrayBitwiseORs(self, nums: List[int]) -> int:
        n = len(nums)

        uniq = {}
        for i in range(n):
            val = 0
            for j in range(i, n):
                val |= nums[j]
                if val in uniq and uniq[val] >= j:
                    break
                uniq[val] = j
        
        return len(uniq)