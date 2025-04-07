# Last updated: 7/4/2025, 6:54:34 pm
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0: return False

        target = total // k
        n = len(nums)

        dp = [[] for _ in range(target+1)]
        
        mask = 1 << n
        full_mask = (1 << (n+1)) - 1
        # print(total, target, full_mask)

        dp[0].append(mask)

        for i, num in enumerate(nums):
            for tot in range(target-num, -1, -1):
                for m in dp[tot]:
                    dp[tot+num].append(m | (1 << i))

        arr = dp[target]

        arr.sort()

        # [print(format(m, f'0{n+5}b')) for m in arr]

        @cache
        def rec(m, index, rem, check):
            # print(m, index, rem, format(check, f'0{n+5}b'), check)

            if rem == 0:
                return check == full_mask
            if index == len(arr): return False

            for i in range(index, len(arr)):
                if m & arr[i] == mask and rec(arr[i], i+1, rem-1, check | arr[i]):
                    return True
            

            return False
        
        for i in range(len(arr)):
            if rec(arr[i], i+1, k-1, mask | arr[i]): return True
        
        return False
