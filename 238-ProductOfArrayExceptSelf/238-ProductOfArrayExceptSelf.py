# Last updated: 12/6/2025, 5:51:10 am
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = []

        prod = 1
        for i in range(n):
            prod *= nums[i]
            ret.append(prod)
        prod = 1 
        for i in range(n-1, 0, -1):
            ret[i] = prod * ret[i-1]
            prod *= nums[i]
        ret[0] = prod
        return ret