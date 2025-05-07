# Last updated: 8/5/2025, 3:08:24 am
mod = 10**9 + 7
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(nums)

        for i in range(n):
            if s[i] == 'L':
                nums[i] -= d
            else:
                nums[i] += d
        
        nums.sort()

        prev = 0
        ret = 0
        for i in range(1, n):
            curr = abs(nums[i] - nums[i-1])
            
            new_prev = (prev + (curr * i % mod)) % mod
            ret = (ret + new_prev) % mod
            prev = new_prev

        return ret