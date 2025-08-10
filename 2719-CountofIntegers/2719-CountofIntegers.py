# Last updated: 10/8/2025, 7:54:13 pm

def substract(x, y):
    carry = 0
    ret = ''
    for i in range(len(x)-1, -1, -1):
        a = int(x[i])
        b = int(y[i])
        if carry:
            carry = (a - 1) < b
            a = (a - 1) % 10
        if b > a:
            carry = 1
            a = 10 + a
        
        ret = str(a - b) + ret
    # print(x, y, ret)
    return ret

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        mod = 10 ** 9 + 7

        m = len(num1)
        n = len(num2)

        def helper(num, length):
            @cache
            def rec(rem, s, is_all, strict):
                if rem == 0:
                    return 1 if s >= min_sum and s <= max_sum else 0
                
                ans = 1 if is_all and s >= min_sum and s <= max_sum else 0

                if strict:
                    for i in range(int(num[length - rem]) + 1):
                        if s == 0 and i == 0: continue
                        
                        if s + i <= max_sum:
                            ans += rec(rem - 1, s + i, is_all, i == int(num[length - rem]))
                else:
                    for i in range(10):
                        if s == 0 and i == 0: continue

                        if s + i <= max_sum:
                            ans += rec(rem - 1, s + i, is_all, strict)
                
                return ans % mod
            
            ans = 0
            if length > 1:
                ans += rec(length - 1, 0, 1, False)

            for i in range(1, min(int(num[0]), max_sum + 1)):
                ans += rec(length - 1, i, 0, False)
                ans %= mod

            if int(num[0]) <= max_sum:
                ans += rec(length - 1, int(num[0]), 0, True)
            
            ans %= mod

            return ans
        
        right = helper(num2, n)
        left = helper(substract(num1, '0' * (m - 1) + '1'), m)

        return (right - left) % mod