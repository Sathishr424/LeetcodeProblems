# Last updated: 7/4/2025, 9:49:03 pm
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0: return False

        target = total // k
        n = len(nums)

        full_mask = (1 << (n+1)) - 1

        @cache
        def rec(tot, mask, done):
            if tot == target:
                done += 1
                if done == k: 
                    return mask == full_mask 
                return rec(0, mask, done)

            for i in range(n):
                if mask & (1 << i) == 0 and nums[i]+tot <= target and rec(tot+nums[i], mask | (1 << i), done):
                    return True
            
            return False

        return rec(0, 1 << n, 0)