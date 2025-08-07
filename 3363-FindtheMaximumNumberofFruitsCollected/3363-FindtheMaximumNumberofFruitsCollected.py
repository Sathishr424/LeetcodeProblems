# Last updated: 7/8/2025, 4:30:04 pm
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        ret = 0
        i = 0
        j = 0
        while i < n:
            ret += fruits[i][j]
            fruits[i][j] = 0
            i += 1
            j += 1
        
        DIR = [[(1, -1), (1, 0), (1, 1)], [(-1, 1), (0, 1), (1, 1)]]
        m = n-1
        def getDis(i, j):
            return max(abs(m - i), abs(m-j))

        @cache
        def dfs(i, j, rem):
            if i == n-1 and j == n-1:
                return [(i, j)], fruits[i][j]
            arr = []
            ans = -inf
            rem -= 1
            for i2, j2 in DIR[0]:
                i2 += i
                j2 += j

                if 0 <= i2 < n and 0 <= j2 < n and getDis(i2, j2) <= rem:
                    new_arr, a = dfs(i2, j2, rem)
                    if a > ans:
                        ans = a
                        arr = new_arr
            arr.append((i, j))
            return arr, ans + fruits[i][j]
        
        @cache
        def dfs2(i, j, rem):
            if i == n-1 and j == n-1:
                return fruits[i][j]
            ans = -inf
            rem -= 1
            for i2, j2 in DIR[1]:
                i2 += i
                j2 += j

                if 0 <= i2 < n and 0 <= j2 < n and getDis(i2, j2) <= rem:
                    a = dfs2(i2, j2, rem)
                    if a > ans:
                        ans = a
            
            return ans + fruits[i][j]
        
        arr, ans = dfs(0, n-1, n-1)
        dfs.cache_clear()
        ret += ans
        # return ans
        for (i, j) in arr:
            fruits[i][j] = 0

        ans = dfs2(n-1, 0, n-1)
        dfs2.cache_clear()
        ret += ans
        return ret