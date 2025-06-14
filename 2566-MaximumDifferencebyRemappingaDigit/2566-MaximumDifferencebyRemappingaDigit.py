# Last updated: 14/6/2025, 3:22:33 pm
@cache
def gcd(x, y):
    rem = x % y
    if rem == 0: return y
    return gcd(y, rem)

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 0

        for num in nums:
            if num == k: ret += 1

        for i in range(n-1):
            num = nums[i]
            for j in range(i+1, n):
                num = gcd(max(num, nums[j]), min(num, nums[j]))
                if num == k:
                    ret += 1
        
        return ret
            