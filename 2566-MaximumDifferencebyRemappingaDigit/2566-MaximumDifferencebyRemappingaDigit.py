# Last updated: 14/6/2025, 2:28:52 pm
def gcd(x, y):
    rem = x % y
    if rem == 0: return y
    return gcd(y, rem)

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x = max(nums)
        y = min(nums)

        return gcd(x, y)