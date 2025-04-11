# Last updated: 11/4/2025, 4:09:48 pm
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ret = 0
        for num in range(low, high+1):
            n = len(str(num))
            if n % 2 != 0: continue
            
            prefix = []
            tot = 0

            while num:
                rem = num % 10
                num //= 10

                tot += rem
                prefix.append(tot)
            
            half = prefix[n // 2 - 1]
            if prefix[-1] - half == half: ret += 1
        
        return ret

