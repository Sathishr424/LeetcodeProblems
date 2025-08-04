# Last updated: 4/8/2025, 2:36:57 pm
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        bits = [0] * 14

        for num in range(1, n + 1):
            bit = 13
            while num:
                if num % 2:
                    bits[bit] += 1
                bit -= 1
                num //= 2
        
        for num in nums:
            bit = 13
            while num:
                if num % 2:
                    bits[bit] -= 1
                bit -= 1
                num //= 2
        
        bit = 13
        ret = 0
        power = 0
        while bit >= 0:
            if bits[bit]:
                ret += 1 << power
            power += 1
            bit -= 1
        
        return ret