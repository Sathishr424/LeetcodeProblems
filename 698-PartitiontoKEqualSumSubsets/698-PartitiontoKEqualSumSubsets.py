# Last updated: 7/4/2025, 7:20:39 pm
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0: return False

        target = total // k
        n = len(nums)

        dp = [[] for _ in range(target+1)]
        
        mask = 1 << n
        full_mask = (1 << (n+1)) - 1

        dp[0].append(mask)

        for i, num in enumerate(nums):
            for tot in range(target-num, -1, -1):
                for m in dp[tot]:
                    dp[tot+num].append(m | (1 << i))

        arr = dp[target]

        dp = {}
        def rec(j, index, rem, check):
            if check in dp: return dp[check]
            if rem == 0:
                return check == full_mask
            if index == len(arr): return False

            for i in range(index, len(arr)):
                if arr[j] & arr[i] == mask and rec(i, i+1, rem-1, check | arr[i]):
                    dp[check] = True
                    return True
            
            dp[check] = False
            return False
        
        for i in range(len(arr)):
            if rec(i, i+1, k-1, mask | arr[i]): return True
        
        return False
