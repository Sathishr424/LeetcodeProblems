# Last updated: 12/25/2025, 7:11:05 PM
@cache
def get2Power(num):
    cnt = 0
    while num % 2 == 0:
        cnt += 1
        num //= 2
    return cnt

cmax = lambda x, y: x if x > y else y
class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = max(nums) * 2

        powers = []
        for num in nums:
            powers.append(get2Power(num))
        
        for i in range(n):
            num = nums[i]
            min_power = powers[i]
            cnt = 1
            for j in range(i+1, n):
                num = gcd(nums[j], num)
                if powers[j] < min_power:
                    cnt = 1
                    min_power = powers[j]
                elif powers[j] == min_power:
                    cnt += 1
                ret = cmax(ret, num * (j-i+1))

                if cnt <= k:
                    ret = cmax(ret, num * 2 * (j-i+1))
        
        return ret
                
