# Last updated: 6/5/2025, 4:53:51 pm
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

        pows = [0] * total
        for i in range(total):
            pows[i] = pow(10, i, k)

        def rec(mask, num, rem, whole_num):
            if mask == 0: return num, []
            
            key = (mask, whole_num)
            if key in memo: return memo[key]

            ans = float('inf')
            ret_arr = []

            for i in range(n):
                if (mask >> i) & 1:
                    new_num = nums[i] * pows[rem - digits[i]] % k
                    new_num, arr = rec(mask & ~(1 << i), new_num, rem - digits[i], (whole_num + new_num) % k)

                    if (whole_num + new_num) % k == 0:
                        ans = (num + new_num) % k
                        ret_arr = [nums[i]] + arr
                        break
            
            memo[key] = [ans, ret_arr]
            return ans, ret_arr
        
        return rec((1 << n) - 1, 0, total, 0)[1]