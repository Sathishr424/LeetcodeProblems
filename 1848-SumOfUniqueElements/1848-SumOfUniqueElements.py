# Last updated: 12/6/2025, 5:40:07 am
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        ret = 0

        for num in nums:
            if hash[num] == 1:
                ret -= num
                hash[num] += 1
            elif hash[num] == 0:
                ret += num
                hash[num] += 1
        
        return ret