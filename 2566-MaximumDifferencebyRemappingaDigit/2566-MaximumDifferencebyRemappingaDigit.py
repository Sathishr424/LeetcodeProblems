# Last updated: 14/6/2025, 3:31:38 pm
def gcd(x, y):
    if y == 0: return x
    return gcd(y, x % y)

# 45 => 10 . 2 + 5
# 10 => 5 . 2 + 0

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 0

        for i in range(n):
            num = 0
            for j in range(i, n):
                ret += (num := gcd(nums[j], num)) == k
        
        return ret
            