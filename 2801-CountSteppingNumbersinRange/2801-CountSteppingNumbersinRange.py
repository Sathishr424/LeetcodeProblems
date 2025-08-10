# Last updated: 10/8/2025, 11:39:55 am
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
    return ret

class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        low = substract(low, '0' * (len(low) - 1) + '1')
        
        l_n = len(low)
        r_n = len(high)
        mod = 10**9 + 7

        @cache
        def rec(rem, prev):
            if rem == 0:
                return 1
            
            ans = 1
            if prev + 1 < 10:
                ans += rec(rem - 1, prev + 1)
            if prev - 1 >= 0:
                ans += rec(rem - 1, prev - 1)
            
            return ans % mod
        
        @cache
        def rec3(rem, prev):
            if rem == 0:
                return 1
        
            ans = 0
            if prev + 1 < 10:
                ans += rec3(rem - 1, prev + 1)
            if prev - 1 >= 0:
                ans += rec3(rem - 1, prev - 1)
            
            return ans % mod
        
        @cache
        def rec2(rem, prev, strict):
            if rem == r_n:
                return 1
        
            ans = 0
            if not strict:
                if prev + 1 < 10:
                    ans += rec2(rem + 1, prev + 1, False)
                if prev - 1 >= 0:
                    ans += rec2(rem + 1, prev - 1, False)
            else:
                if prev + 1 < 10 and prev + 1 <= int(high[rem]):
                    ans += rec2(rem + 1, prev + 1, prev + 1 == int(high[rem]))
                if prev - 1 >= 0 and prev - 1 <= int(high[rem]):
                    ans += rec2(rem + 1, prev - 1, prev - 1 == int(high[rem]))
            
            return ans % mod

        @cache
        def rec4(rem, prev, strict):
            if rem == l_n:
                return 1
        
            ans = 0
            if not strict:
                if prev + 1 < 10:
                    ans += rec4(rem + 1, prev + 1, False)
                if prev - 1 >= 0:
                    ans += rec4(rem + 1, prev - 1, False)
            else:
                if prev + 1 < 10 and prev + 1 <= int(low[rem]):
                    ans += rec4(rem + 1, prev + 1, prev + 1 == int(low[rem]))
                if prev - 1 >= 0 and prev - 1 <= int(low[rem]):
                    ans += rec4(rem + 1, prev - 1, prev - 1 == int(low[rem]))
            
            return ans % mod
        
        ans = 0
        if r_n >= 2:
            for i in range(1, 10):
                ans += rec(r_n - 2, i)
                ans %= mod

        for i in range(1, int(high[0])):
            ans += rec3(r_n - 1, i)
            ans %= mod
        
        ans += rec2(1, int(high[0]), True)
        ans %= mod

        left = 0
        if l_n >= 2:
            for i in range(1, 10):
                left += rec(l_n - 2, i)
                left %= mod
        
        for i in range(1, int(low[0])):
            left += rec3(l_n - 1, i)
            left %= mod
        
        if int(low[0]) > 0:
            left += rec4(1, int(low[0]), True)
            left %= mod
        
        rec.cache_clear()
        rec2.cache_clear()
        rec3.cache_clear()
        rec4.cache_clear()
        return (ans - left) % mod