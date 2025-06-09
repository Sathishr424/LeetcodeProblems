# Last updated: 10/6/2025, 3:09:55 am
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def dfs(num, rem):
            if rem == 0: return num // 10

            cnt = 0
            for i in range(10):
                new_num = num + i
                possible = getPossible(new_num)

                if cnt + possible >= rem:
                    return dfs(new_num * 10, rem-cnt-1)
                
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
        for i in range(1, 10):
            possible = getPossible(i)
            if cnt + possible >= k:
                return dfs(i * 10, k-cnt-1)
            cnt += possible

        return 0