# Last updated: 26/4/2025, 2:08:49 am
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ret = 0

        prefix = {}
        prefix[0] = -1

        # 01011110100
        # 01011110100
        cnt = 0
        for i, num in enumerate(nums):
            if num: cnt += 1
            else: cnt -= 1
            
            if cnt in prefix:
                ret = max(ret, i-prefix[cnt])
            elif cnt not in prefix:
                prefix[cnt] = i
        
        return ret
