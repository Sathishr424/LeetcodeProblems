# Last updated: 8/4/2025, 4:45:53 am
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        target = total // k

        if total / k != target: return False

        n = len(nums)

        full_mask = (1 << (n+1)) - 1

        dp = {}
        nums.sort()
        
        def rec(index, tot, mask, done):
            if mask in dp: return False
            
            index = index % n

            for i in range(index, n):
                if nums[i]+tot <= target:
                    if mask & (1 << i) == 0:
                        if nums[i]+tot == target:
                            if done+1 == k: return mask | (1 << i) == full_mask 
                            return rec(0, 0, mask | (1 << i), done+1)

                        if rec(i+1, tot+nums[i], mask | (1 << i), done):
                            return True
                else:
                    break
            
            dp[mask] = True

            return False

        return rec(0, 0, 1 << n, 0)