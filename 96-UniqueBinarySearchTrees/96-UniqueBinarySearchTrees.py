# Last updated: 5/8/2025, 12:11:06 pm
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 0
        for i in range(n):
            d = nums[i]
            for j in range(i, n):
                d = gcd(nums[j], d)
                if d == k: ret += 1
        
        return ret