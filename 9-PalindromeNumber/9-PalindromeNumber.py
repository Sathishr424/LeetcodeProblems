# Last updated: 4/8/2025, 11:15:59 pm
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = [0] * 101

        for num in nums:
            freq[num] += 1

        ret = 0
        for cnt in freq:
            if cnt > 1:
                ret += cnt * (cnt - 1) // 2
        
        return ret