# Last updated: 10/8/2025, 6:08:49 am
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        length = 0

        tmp = n
        digits = []
        while tmp:
            length += 1
            digits.append(tmp % 10)
            tmp //= 10
        
        l = 0
        r = 31
        digits.sort()
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

            match = True
            for i in range(length):
                if val[i] != digits[i]:
                    match = False
                    break
            if match: return True
            l += 1
        
        return False