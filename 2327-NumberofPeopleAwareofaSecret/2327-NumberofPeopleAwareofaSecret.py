# Last updated: 9/9/2025, 1:02:44 pm
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7

        @cache
        def rec(day, f_day):
            if day == f_day:
                return 0
            if day == n: 
                return 2
            elif day > n:
                return 1
            
            return (rec(day + 1, f_day) + rec(day + delay, day + forget)) % mod
        
        ans = rec(1 + delay, 1 + forget)
        rec.cache_clear()
        return ans