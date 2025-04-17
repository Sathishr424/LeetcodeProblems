# Last updated: 17/4/2025, 8:14:02 am
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j] and i * j % k == 0: ret += 1
        
        return ret