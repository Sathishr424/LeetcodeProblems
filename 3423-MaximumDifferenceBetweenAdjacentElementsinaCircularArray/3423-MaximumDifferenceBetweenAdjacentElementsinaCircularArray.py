# Last updated: 12/6/2025, 3:29:43 pm
cmax = lambda x, y: x if x > y else y
cmin = lambda x, y: x if x < y else y
inf = 30000

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        there = [0] * 5

        for char in s:
            there[int(char)] = 1

        def calc(x, y):
            prefix = [[inf, inf, inf, inf] for _ in range(n+1)]
            odd = 0
            even = 0

            for i in range(n):
                if s[i] == x:
                    odd += 1
                elif s[i] == y:
                    even += 1
                
                add = ((odd % 2) * 2) + (even % 2)
                for index in range(4):
                    if index == add:
                        prefix[i+1][index] = cmin(prefix[i][index], odd-even)
                    else:
                        prefix[i+1][index] = prefix[i][index]
            odd = 0
            even = 0
            ans = -inf
            
            even_prev_1 = -1
            even_prev = -1

            odd_prev = -1

            i = 0
            while i < n and (i < k-1 or even < 2 or odd == 0):
                if s[i] == x:
                    odd += 1
                    odd_prev = i
                elif s[i] == y:
                    even += 1
                    even_prev_1 = even_prev
                    even_prev = i
                i += 1
            
            if i >= k:
                start = cmin(i-k, cmin(even_prev_1, odd_prev))

                if even % 2 == 0 and odd % 2:
                    ans = cmax(ans, odd - even)
                if start >= 0:
                    index = ((odd + 1) % 2) * 2 + (even % 2)
                    ans = cmax(ans, (odd - even) - prefix[start][index])
            
            for i in range(i, n):
                if s[i] == x:
                    odd += 1
                    odd_prev = i
                elif s[i] == y:
                    even += 1
                    even_prev_1 = even_prev
                    even_prev = i
                
                start = cmin(i-k+1, cmin(even_prev_1, odd_prev))

                if even % 2 == 0 and odd % 2:
                    ans = cmax(ans, odd - even)
                if start >= 0:
                    index = ((odd + 1) % 2) * 2 + (even % 2)
                    ans = cmax(ans, (odd - even) - prefix[start][index])

            return ans

        ret = -inf
        for i in range(5):
            for j in range(5):
                if there[i] == 0 or there[j] == 0 or i == j: continue
                ret = cmax(calc(str(i), str(j)), ret)

        return ret