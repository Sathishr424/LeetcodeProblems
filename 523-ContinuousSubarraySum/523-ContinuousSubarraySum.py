# Last updated: 17/7/2025, 5:54:02 pm
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        for i in range(n):
            nums[i] %= k

        ret = 1
        counter = {}
        tot = 0
        for i in range(n):
            tot = (tot + nums[i]) % k

            need = (k - tot) % k
            # print(nums[:i+1], tot, need, counter)

            if tot in counter:
                ret = max(ret, i - counter[tot])
                # if ret >= 2: return True
            
            if tot == 0: 
                ret = i + 1
                # if ret >= 2: return True
            
            if tot not in counter:
                counter[tot] = i

        return ret >= 2