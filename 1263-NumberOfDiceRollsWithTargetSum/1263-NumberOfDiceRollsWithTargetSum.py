# Last updated: 12/6/2025, 5:43:20 am
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # 1, 2, 3, 4, 5, 6
        # 1, 2, 3, 4, 5, 6
        # 1, 2, 3, 4, 5, 6
        # 1, 2, 3, 4, 5, 6
        # 1, 2, 3
        # 1, 3, 2
        # 2, 1, 3
        # 2, 3, 1
        # 3, 1, 2
        # 3, 2, 1
        # 12
        mod = 10**9 + 7
        ret = 0
        memo = {}
        def rec(sum, turn):
            if (sum, turn) in memo: return memo[(sum, turn)]
            if turn == 0: return sum == target
            ans = 0
            for i in range(1, k+1):
                if i+sum <= target:
                    ans += rec(sum+i, turn-1)
            ans %= mod
            memo[(sum, turn)] = ans
            return ans
        return rec(0, n)