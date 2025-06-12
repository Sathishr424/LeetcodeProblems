# Last updated: 12/6/2025, 5:33:40 am
class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nums.sort()

        digits = []
        total = 0
        for i, num in enumerate(nums):
            digits.append(len(str(num)))
            total += digits[-1]

        pows = [0] * total
        for i in range(total):
            pows[i] = pow(10, i, k)

        start_mask = (1 << n) - 1

        dp = [[None for _ in range(k)] for _ in range(start_mask+1)]

        for i in range(n):
            new_mask = start_mask & ~(1 << i)
            num = nums[i] * pows[total - digits[i]] % k

            dp[new_mask][num % k] = ([nums[i]], total - digits[i])

        for mask in range(start_mask, 0, -1):
            for whole_num in range(k):
                if dp[mask][whole_num] == None: continue
                
                arr, rem = dp[mask][whole_num]
                for i in range(n):
                    if (mask >> i) & 1 == 0: continue

                    new_mask = mask & ~(1 << i)
                    
                    l = digits[i]
                    r = ((nums[i] * pows[rem - l] % k) + whole_num) % k

                    if dp[new_mask][r] == None or arr < dp[new_mask][r][0]:
                        dp[new_mask][r] = (arr + [nums[i]], rem - l)

        return dp[0][0][0] if dp[0][0] != None else []




                        