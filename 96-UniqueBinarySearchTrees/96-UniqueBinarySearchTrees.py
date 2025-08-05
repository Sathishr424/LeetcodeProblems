# Last updated: 5/8/2025, 11:59:09 am
def gcd(x, y):
    rem = x % y
    if rem == 0: return y
    return gcd(y, rem)

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(max(nums), min(nums))