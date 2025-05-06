# Last updated: 6/5/2025, 7:21:05 pm
class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nums.sort()

        # Precompute digit lengths
        digits = [len(str(num)) for num in nums]
        total_digits = sum(digits)

        # Precompute 10^i % k
        pow10 = [1] * (total_digits + 1)
        for i in range(1, total_digits + 1):
            pow10[i] = pow(10, i, k)

        # Initialize DP table
        dp = [[None for _ in range(k)] for _ in range(1 << n)]

        # Base case: each starting number
        for i in range(n):
            mask = (1 << i)
            rem_digits = total_digits - digits[i]
            mod = nums[i] * pow10[rem_digits] % k
            dp[mask][mod] = ([nums[i]], rem_digits)

        # Lex compare
        def is_better(x, y):
            return x < y  # Python list comparison is lexicographic

        # Fill DP
        for mask in range(1 << n):
            for rem in range(k):
                if dp[mask][rem] is None:
                    continue
                seq, rem_digits = dp[mask][rem]

                for i in range(n):
                    if not (mask & (1 << i)):
                        next_mask = mask | (1 << i)
                        new_rem_digits = rem_digits - digits[i]
                        add = nums[i] * pow10[new_rem_digits] % k
                        new_rem = (rem + add) % k
                        new_seq = seq + [nums[i]]

                        if (
                            dp[next_mask][new_rem] is None or
                            is_better(new_seq, dp[next_mask][new_rem][0])
                        ):
                            dp[next_mask][new_rem] = (new_seq, new_rem_digits)

        # Final answer
        full_mask = (1 << n) - 1
        return dp[full_mask][0][0] if dp[full_mask][0] else []
