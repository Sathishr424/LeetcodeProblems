# Last updated: 17/7/2025, 5:56:48 pm
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        counter = {}
        counter[0] = -1
        tot = 0
        for i in range(n):
            tot = (tot + nums[i]) % k

            if tot in counter and i - counter[tot] >= 2: return True
            
            if tot not in counter:
                counter[tot] = i

        return False