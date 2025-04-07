# Last updated: 7/4/2025, 11:14:52 pm
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        target = total // k

        if total / k != target: return False

        n = len(nums)

        mask = 1 << n
        full_mask = (1 << (n+1)) - 1

        def rec(index, tot, done):
            nonlocal mask
            if index == n: return False

            for i in range(index, n):
                if mask & (1 << i) == 0 and tot+nums[i] <= target:
                    curr = tot+nums[i]
                    tmp = mask
                    mask |= 1 << i
                    if curr == target:
                        if done+1 == k: return mask == full_mask
                        return rec(0, 0, done+1)
                    elif rec(i+1, tot+nums[i], done): return True
                    mask = tmp

            return False
        
        return rec(0, 0, 0)

