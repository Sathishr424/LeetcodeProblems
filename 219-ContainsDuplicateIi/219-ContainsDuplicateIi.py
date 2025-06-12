# Last updated: 12/6/2025, 5:51:32 am
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}
        for i, num in enumerate(nums):
            if num in hash and i-hash[num] <= k: return True
            hash[num] = i
        return False