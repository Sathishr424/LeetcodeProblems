# Last updated: 12/25/2025, 7:10:52 PM
class Solution:
    def concatHex36(self, n: int) -> str:
        tmp = n * n
        ret = ''
        while tmp:
            rem = tmp % 16
            if rem <= 9:
                ret += str(rem)
            else:
                ret += chr(ord('A') + (rem - 10))
            tmp //= 16
        
        ret = ret[::-1]
        
        tmp = n * n * n
        curr = ''
        while tmp:
            rem = tmp % 36
            if rem <= 9:
                curr += str(rem)
            else:
                curr += chr(ord('A') + (rem - 10))
            tmp //= 36

        return ret + curr[::-1]