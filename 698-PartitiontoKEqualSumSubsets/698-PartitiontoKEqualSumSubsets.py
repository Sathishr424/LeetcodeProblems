# Last updated: 8/4/2025, 4:47:27 am
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
                curr = nums[i]+tot
                if curr <= target:
                    if mask & (1 << i) == 0:
                        if curr == target:
                            if done+1 == k: return mask | (1 << i) == full_mask 
                            return rec(0, 0, mask | (1 << i), done+1)

                        elif rec(i+1, curr, mask | (1 << i), done):
                            return True
                else:
                    break
            
            dp[mask] = True

            return False

        return rec(0, 0, 1 << n, 0)