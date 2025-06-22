# Last updated: 23/6/2025, 3:29:28 am
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        
        @cache
        def rec(index, target):
            if target == 0:
                return 1
            if index == n or target - coins[index] < 0: return 0

            return rec(index+1, target) + rec(index, target - coins[index])
        
        return rec(0, amount)