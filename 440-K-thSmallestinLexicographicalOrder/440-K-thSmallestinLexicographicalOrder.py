# Last updated: 10/6/2025, 3:04:48 am
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def dfs(num, rem):
            if rem == 0: return num // 10
            # print(num, rem, l_)
            x = 0
            for i in range(10):
                new_num = num + i

                z = getL(new_num)
                prev = x
                x += z
                if x >= rem:
                    # print((num, rem, z), new_num, i, (x, z))
                    return dfs(new_num * 10, rem-prev-1)
                # print(new_num, (x, z))

        def getL(num):
            dig = 1
            add = 1
            while num * (dig * 10) + (dig * 10 - 1) <= n:
                dig *= 10
                add += dig
            
            b = num * dig * 10
            return ( add ) + ((n % b) + 1 if n - (n % b) == b else 0)

        x = 0
        for i in range(1, 10):
            new_l = getL(i)
            if x + new_l >= k:
                return dfs(i * 10, k-x-1)
            x += new_l
            # print(i, x, new_l)

        return 0