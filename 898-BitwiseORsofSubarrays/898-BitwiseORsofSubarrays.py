# Last updated: 31/7/2025, 1:41:55 pm
class Solution:
    def subarrayBitwiseORs(self, nums: List[int]) -> int:
        n = len(nums)

        uniq = {}

        for i in range(n):
            val = 0
            new_uniq = {}
            for j in range(i, n):
                val |= nums[j]
                if val in uniq and uniq[val] >= j: 
                    # print((i, j), val, uniq)
                    break
                new_uniq[val] = j
            
            for num in new_uniq:
                if num not in uniq:
                    uniq[num] = new_uniq[num]
        
        return len(uniq)