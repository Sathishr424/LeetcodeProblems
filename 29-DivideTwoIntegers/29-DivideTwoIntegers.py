# Last updated: 17/7/2025, 2:25:04 pm
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_neg = 0
        if divisor < 0:
            divisor = -divisor
            is_neg += 1
        if dividend < 0:
            dividend = -dividend
            is_neg += 1
        
        num = 0
        add = divisor
        op = 0
        op_add = 1
        while True:
            if num + add > dividend:
                if op_add == 1: break
                add = divisor
                op_add = 1
                continue
            
            num += add
            add += add
            op += op_add
            op_add += op_add
        
        if is_neg == 1: 
            return -min(op, 2**31)
        return min(op, 2**31 - 1)