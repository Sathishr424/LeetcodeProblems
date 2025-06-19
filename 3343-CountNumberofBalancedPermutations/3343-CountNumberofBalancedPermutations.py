# Last updated: 19/6/2025, 8:57:56 am
mod = 10 ** 9 + 7
@cache
def inverse(x):
    x = fact(x)
    return pow(x, mod-2, mod)

@cache
def fact(x):
    if x == 0: return 1
    return fact(x-1) * x % mod

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        half = n // 2
    
        arr = [int(a) for a in num]
        arr.sort()

        total = sum(arr)
        target = total // 2

        if total % 2: return 0
        uniq = [0] * 10
        
        for a in arr:
            uniq[a] += 1

        f = fact(half)
        f2 = fact(n - half)

        combined = f * f2 % mod

        dp = [[[-1] * 361 for _ in range(half+1)] for _ in range(11)]

        def howmany(index, cnt, tot):
            if dp[index][cnt][tot] != -1: return dp[index][cnt][tot]
            if index == 10 and cnt == 0 and tot == 0:
                return combined
            if index == 10 or tot < 0: return 0
            ans = 0
            r = uniq[index]
            
            new_tot = tot
            new_cnt = cnt
            for l in range(r+1):
                if new_tot < 0 or new_cnt < 0:
                    break
                ans += inverse(l) * inverse(r-l) * howmany(index+1, new_cnt, new_tot)
                ans %= mod
                new_tot -= index
                new_cnt -= 1
            dp[index][cnt][tot] = ans
            return ans
            
        return howmany(0, half, target)