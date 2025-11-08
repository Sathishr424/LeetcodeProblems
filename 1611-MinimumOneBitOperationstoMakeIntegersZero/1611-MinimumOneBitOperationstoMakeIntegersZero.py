# Last updated: 8/11/2025, 4:47:29 pm
powers = [1]
for i in range(31):
    powers.append(powers[-1] * 2 + 1)

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        power = 0
        ans = 0
        while n:
            if n & 1:
                ans = powers[power] - ans
            
            n >>= 1
            power += 1
        
        return ans