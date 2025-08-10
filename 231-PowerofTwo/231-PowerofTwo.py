# Last updated: 10/8/2025, 5:57:11 am
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        length = 0

        tmp = n
        digits = []
        while tmp:
            length += 1
            digits.append(tmp % 10)
            tmp //= 10
        
        full_mask = (1 << length) - 1

        @cache
        def rec(mask, num):
            if mask == full_mask:
                if num > 0 and num & (num - 1) == 0: return True
                return False
            
            for i in range(length):
                if digits[i] == 0 and num == 0: continue
                if mask & (1 << i) == 0 and rec(mask | (1 << i), num * 10 + digits[i]):
                    return True
            
            return False
        
        return rec(0, 0)
