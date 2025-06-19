# Last updated: 19/6/2025, 10:00:30 am
class Solution:
    def totalFruit(self, f: List[int]) -> int:
        n = len(f)

        basket = {}
        basket[f[0]] = 0
        i = 1
        while i < n and f[i] == f[0]:
            i += 1
        
        if i == n: return n

        basket[f[0]] = i-1
        basket[f[i]] = i
        ret = i + 1
        cnt = i + 1

        for i in range(i+1, n):
            if f[i] not in basket:
                x, y = list(basket.keys())

                if basket[x] > basket[y]:
                    cnt = i - basket[y]
                    del basket[y]
                else:
                    cnt = i - basket[x]
                    del basket[x]
            else:
                cnt += 1
            
            basket[f[i]] = i
            ret = max(ret, cnt)
        
        return ret




        