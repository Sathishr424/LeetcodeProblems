# Last updated: 12/6/2025, 5:51:34 am
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for n in nums:
            if n in hash:
                hash[n] += 1
                if hash[n] >= 2: return True
            else:
                hash[n] = 1
        return False