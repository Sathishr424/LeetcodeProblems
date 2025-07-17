# Last updated: 17/7/2025, 2:23:17 pm
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_neg = 0
        if divisor < 0:
            divisor = -divisor
            is_neg += 1
        if dividend < 0:
            dividend = -dividend
            is_neg += 1
        
        def recAdd(num, add, op, op_add):
            if num + add > dividend:
                if op_add == 1: return op
                return recAdd(num, divisor, op, 1)
            
            return recAdd(num + add, add + add, op + op_add, op_add + op_add)
        

        ans = recAdd(0, divisor, 0, 1)
        if is_neg == 1: 
            return -min(ans, 2**31)
        return min(ans, 2**31 - 1)