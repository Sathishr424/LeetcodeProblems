# Last updated: 6/5/2025, 2:20:53 pm
class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nums.sort()
        digits = []

        total = 0
        for i, num in enumerate(nums):
            l = len(str(num))
            digits.append(l)
            total += l

        memo = {}

        def rec(mask, num, rem, need):
            if mask == 0:
                return num, []
            
            key = (mask, num, need)
            if key in memo: return memo[key]

            ans = float('inf')
            ret_arr = []

            for i in range(n):
                if (mask >> i) & 1:
                    num2 = nums[i] * pow(10, rem - digits[i], k) % k

                    new_num, arr = rec(mask & ~(1 << i), num2, rem - digits[i], (need + num) % k)

                    if (need + num + new_num) % k == 0:
                        ans = (num + new_num) % k
                        ret_arr = [nums[i]] + arr
                        break
            
            memo[key] = [ans, ret_arr]
            return ans, ret_arr
        
        return rec((1 << n)-1, 0, total, 0)[1]