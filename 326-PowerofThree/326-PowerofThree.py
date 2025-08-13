# Last updated: 13/8/2025, 10:52:31 am
powers = [0] * 22

for i in range(22):
    powers[i] = 3 ** i

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False

        x = 0
        while powers[x] < n:
            x += 1
        
        return powers[x] == n
