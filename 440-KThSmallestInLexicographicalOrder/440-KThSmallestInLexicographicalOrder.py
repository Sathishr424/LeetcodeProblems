# Last updated: 12/6/2025, 5:49:26 am
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def dfs(num, rem):
            if rem == 0: return num
            
            num *= 10
            cnt = 0

            for new_num in range(num, num+10):
                possible = getPossible(new_num)

                if cnt + possible >= rem:
                    return dfs(new_num, rem-cnt-1)
                
                cnt += possible

        def getPossible(num):
            digits = 1
            possible = 1

            while num * digits + (digits - 1) <= n:
                digits *= 10
                possible += digits
            
            possible -= digits
            digits //= 10

            balance = num * digits * 10
            return possible + ((n % balance) + 1 if n - (n % balance) == balance else 0)

        cnt = 0
        for num in range(1, 10):
            possible = getPossible(num)
            if cnt + possible >= k:
                return dfs(num, k-cnt-1)
            cnt += possible

        return 0