# Last updated: 6/5/2025, 7:15:59 pm
def compare(x, y):
    for i in range(len(x)):
        if x[i] < y[i]: return True
        elif y[i] < x[i]: return False
    
    return False

class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nums.sort()
        digits = [0] * n

        for i in range(n):
            digits[i] = len(str(nums[i]))
        
        total = sum(digits)

        pows = [0] * total
        for i in range(total):
            pows[i] = pow(10, i, k)
        
        start_mask = (1 << n) - 1

        dp = [[[] for _ in range(k)] for _ in range(start_mask+1)]

        for i in range(n):
            new_mask = start_mask & ~(1 << i)
            num = nums[i] * pows[total - digits[i]] % k

            dp[new_mask][num % k] = [nums[i], (total - digits[i])]

        for mask in range(start_mask, 0, -1):
            for rem in range(k):
                
                if not dp[mask][rem]: continue
                arr = dp[mask][rem][:-1]
                d = dp[mask][rem][-1]

                for i in range(n):
                    if (mask >> i) & 1 == 0: continue

                    new_mask = mask & ~(1 << i)

                    r = ((nums[i] * pows[d - digits[i]] % k) + rem) % k

                    if not dp[new_mask][r] or compare(arr, dp[new_mask][r]):
                        dp[new_mask][r] = arr + [nums[i], d-digits[i]]

        return dp[0][0][:-1] if dp[0][0] else []




                        