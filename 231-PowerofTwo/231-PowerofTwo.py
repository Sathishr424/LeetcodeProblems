# Last updated: 10/8/2025, 6:14:03 am
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = []
        while n:
            digits.append(n % 10)
            n //= 10
        digits.sort()
        
        length = len(digits)
        l = 0
        r = 31
        while l < r:
            mid = (l + r) // 2

            if len(str(1 << mid)) >= length:
                r = mid
            else:
                l = mid + 1
        
        while len(str(1 << l)) == length:
            val = []
            num = 1 << l
            while num:
                val.append(num % 10)
                num //= 10
            val.sort()

            for i in range(length):
                if val[i] != digits[i]: break
            else:
                return True
            l += 1
        
        return False