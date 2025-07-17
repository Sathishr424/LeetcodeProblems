# Last updated: 17/7/2025, 5:55:38 pm
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        counter = {}
        tot = 0
        for i in range(n):
            tot = (tot + nums[i]) % k

            need = (k - tot) % k

            if tot in counter and i - counter[tot] >= 2: return True
            if tot == 0 and i >= 1: return True 
            
            if tot not in counter:
                counter[tot] = i

        return False