# Last updated: 11/4/2025, 4:14:51 pm
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ret = 0
        for num in range(low, high+1):
            if len(str(num)) % 2 != 0: continue
            
            prefix = []
            tot = 0

            while num:
                tot += num % 10
                num //= 10

                prefix.append(tot)
            
            half = prefix[len(prefix) // 2 - 1]
            if prefix[-1] - half == half: ret += 1
        
        return ret

