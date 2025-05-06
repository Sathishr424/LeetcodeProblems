# Last updated: 6/5/2025, 5:58:33 pm
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

        start_mask = (1 << n) - 1

        dp = [[[[], total] for _ in range(k)] for _ in range(start_mask+1)]

        for i in range(n):
            new_mask = start_mask & ~(1 << i)
            num = nums[i] * pows[total - digits[i]] % k

            dp[new_mask][num % k] = [[nums[i]], total - digits[i]]

        def compare(x, y):
            for i in range(len(x)):
                if x[i] < y[i]: return True
                elif y[i] < x[i]: return False
            
            return False

        for mask in range(start_mask, 0, -1):
            for whole_num in range(k):
                arr, rem = dp[mask][whole_num]
                if rem == total: continue
                for i in range(n):
                    if (mask >> i) & 1 == 0: continue

                    new_mask = mask & ~(1 << i)
                    l = digits[i]

                    num = nums[i] * pows[rem - l] % k
                    r = (num + whole_num) % k

                    if dp[new_mask][r][1] == total:
                        dp[new_mask][r] = [arr + [nums[i]], rem - l]
                    else:
                        new_arr = arr + [nums[i]]
                        old_arr = dp[new_mask][r][0]
                        
                        # print(new_arr, old_arr)

                        if compare(new_arr, old_arr):
                            dp[new_mask][r] = [new_arr, rem - l]

        # print(dp[0])
        return dp[0][0][0]




                        