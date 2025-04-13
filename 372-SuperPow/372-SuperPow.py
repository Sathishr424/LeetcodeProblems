# Last updated: 13/4/2025, 7:26:15 pm
class Solution:
    def superPow(self, x: int, b: List[int]) -> int:
        mod = 1337

        n = int(''.join([str(i) for i in b]))
    
        def rec(n):
            if n == 0: return 1
            elif n == 1: return x

            ans = rec(n//2)
            
            if n % 2 == 0:
                return ans * ans % mod
            else:
                ans = ans * ans % mod
                return ans * x % mod
        
        return rec(n)


        