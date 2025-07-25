# Last updated: 26/5/2025, 1:43:54 pm
cmax = lambda x, y: x if x > y else y
cmin = lambda x, y: x if x < y else y
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ret = nums[0]

        mn = ret
        mx = ret

        for i in range(1, n):
            new_mn = nums[i] * mn
            new_mx = nums[i] * mx
            mn = min(nums[i], new_mn, new_mx)
            mx = max(nums[i], new_mn, new_mx)
            
            ret = cmax(mx, ret)
        
        return ret
        