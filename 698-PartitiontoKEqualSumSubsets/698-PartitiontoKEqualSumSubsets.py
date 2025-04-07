# Last updated: 7/4/2025, 9:59:36 pm
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        target = total // k

        if total / k != target: return False

        n = len(nums)

        full_mask = (1 << (n+1)) - 1

        dp = {}
        for i in range(1 << n, full_mask+1):
            dp[i] = False

        def rec(index, tot, mask, done):
            if tot == target:
                done += 1
                if done == k: return mask == full_mask 
                return rec(0, 0, mask, done)
            
            if dp[mask]: return False
            index = index % n

            for i in range(index, n):
                if mask & (1 << i) == 0 and nums[i]+tot <= target and rec(i+1, tot+nums[i], mask | (1 << i), done):
                    return True

            dp[mask] = True

            return False

        return rec(0, 0, 1 << n, 0)