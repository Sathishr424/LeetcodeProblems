# Last updated: 17/7/2025, 2:19:21 pm
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # if dividend == 0: return 0
        # if divisor == 1: return dividend
        # if divisor > dividend: return 0
        # if divisor == dividend: return 1

        is_neg = (divisor < 0) + (dividend < 0)
        divisor = abs(divisor)   
        dividend = abs(dividend)   
        
        def recAdd(num, add, op, op_add):
            # print("add", (num, add, op, op_add))
            if num + add > dividend:
                if op_add == 1: return op
                return recAdd(num, divisor, op, 1)
            
            return recAdd(num + add, add + add, op + op_add, op_add + op_add)
        

        ans = recAdd(0, divisor, 0, 1)
        if is_neg == 1: 
            return -min(ans, 2**31)
        return min(ans, 2**31 - 1)