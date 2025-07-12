# Last updated: 13/7/2025, 12:49:48 am
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % k: return False

        nums.sort()
        half = total // k
        full_mask = (1 << n) - 1

        @cache
        def rec(mask, rem_tot, rem):
            if mask == full_mask:
                if rem == 1 and rem_tot == 0: return True
                return False
            if rem == 0: return False
            if rem_tot == 0:
                return rec(mask, half, rem - 1)
            
            for i in range(n):
                if nums[i] > rem_tot: break
                if mask & (1 << i) == 0:
                    if rec(mask | (1 << i), rem_tot - nums[i], rem):
                        return True
            
            return False

        ans = rec(0, half, k)
        rec.cache_clear()
        return ans
        