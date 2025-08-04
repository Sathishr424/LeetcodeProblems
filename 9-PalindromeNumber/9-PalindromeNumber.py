# Last updated: 4/8/2025, 10:48:35 pm
def addition(a, b):
    max_int = 1 << 32
    ret = 0
    carry = 0
    power = 0
    while power < 32:
        a_rem = a % 2
        b_rem = b % 2

        if a_rem and b_rem:
            if carry:  ret += 1 << power
            else: carry = 1
        elif a_rem or b_rem:
            if not carry: ret += 1 << power
        elif carry:
            ret += 1 << power
            carry = 0
        power += 1
        a //= 2
        b //= 2
    
    if carry: ret += 1 << power
    if a < 0: ret = ret - max_int
    if b < 0: ret = ret - max_int
    return ret

class Solution:
    def getSum(self, a: int, b: int) -> int:
        return addition(a, b)