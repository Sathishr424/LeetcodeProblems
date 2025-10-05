# Last updated: 5/10/2025, 10:06:34 pm
class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        nums = [int(num) for num in str(n)]
        m = len(nums)

        def check(index, carry):
            for j in range(index, -1, -1):
                a = nums[j] - carry
                if a < 0:
                    if j == 0: return 0
                    a = nums[j] + 10 - carry
                    carry = 1
                else:
                    carry = 0
                if a == 0 and j > 0: return 0
            return 1
        
        @cache
        def rec(index, carry, last_zero):
            if index == -1:
                return (carry + 1) & 1
            if last_zero:
                return check(index, carry)

            ans = 0
            if index != m-1 and check(index, carry):
                ans += 1
            
            for b in range(1, 10):
                a = nums[index] - carry
                new_carry = 0
                if a < b:
                    if index == 0: break
                    a = nums[index] + 10 - carry
                    new_carry = 1
                
                if a == b:
                    if index != m-1:
                        ans += rec(index - 1, new_carry, 1)
                else:
                    ans += rec(index - 1, new_carry, 0)
            
            return ans

        ans = rec(m-1, 0, 0)
        rec.cache_clear()
        return ans
        