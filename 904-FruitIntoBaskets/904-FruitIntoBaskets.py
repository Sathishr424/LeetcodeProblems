# Last updated: 19/6/2025, 10:03:38 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def totalFruit(self, f: List[int]) -> int:
        n = len(f)

        a = f[0]
        i = 1
        while i < n and f[i] == a:
            i += 1
        
        if i == n: return n
        b = f[i]

        a_cnt = i
        b_cnt = 1
        ret = a_cnt + b_cnt
    
        cnt = 1
        prev = f[i]

        for i in range(i+1, n):
            if f[i] == a:
                a_cnt += 1
            elif f[i] == b:
                b_cnt += 1
            else:
                if prev == a:
                    a_cnt = cnt
                    b_cnt = 1
                    b = f[i]
                else:
                    a_cnt = 1
                    b_cnt = cnt
                    a = f[i]
            
            if f[i] == prev:
                cnt += 1
            else:
                prev = f[i]
                cnt = 1
            
            ret = cmax(a_cnt + b_cnt, ret)
        
        return ret

        