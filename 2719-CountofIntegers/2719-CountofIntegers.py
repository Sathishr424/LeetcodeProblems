# Last updated: 10/8/2025, 8:38:14 pm
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        low = str(low - 1)
        high = str(high)

        def helper(num, length):
            @cache
            def rec(rem, curr_num, odd, is_all, tight):
                if rem == length - is_all:
                    return 1 if curr_num == 0 and odd == (rem - odd) else 0
                
                ans = 1 if is_all and curr_num == 0 and odd == (rem - odd) else 0

                if tight:
                    for i in range(int(num[rem]) + 1):
                        ans += rec(rem + 1, (curr_num * 10 + i) % k, odd + (i % 2), is_all, i == int(num[rem]))
                else:
                    for i in range(10):
                        ans += rec(rem + 1, (curr_num * 10 + i) % k, odd + (i % 2), is_all, False)
                
                return ans
            
            ans = 0
            if length > 1:
                for i in range(1, 10):
                    ans += rec(1, i % k, i % 2, 1, False)

            for i in range(1, int(num[0]) + 1):
                ans += rec(1, i % k, i % 2, 0, i == int(num[0]))
            
            rec.cache_clear()
            return ans
        
        right = helper(high, len(high))
        left = helper(low, len(low))

        return right - left