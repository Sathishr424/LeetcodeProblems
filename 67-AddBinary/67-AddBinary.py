# Last updated: 12/6/2025, 5:54:04 am
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a)
        n = len(b)

        if n > m:
            a, b = b, a
            m, n = n, m
        
        carry = 0
        ret = ''
        for i in range(n):
            val = int(a[m-i-1]) + int(b[n-i-1]) + carry
        
            if val == 2:
                ret += '0'
                carry = 1
            elif val == 3:
                ret += '1'
                carry = 1
            else:
                ret += str(val)
                carry = 0

        for i in range(m-n-1, -1, -1):
            val = int(a[i]) + carry
        
            if val == 2:
                ret += '0'
                carry = 1
            else:
                ret += str(val)
                carry = 0
        if carry: ret += '1'
        return ret[::-1]
