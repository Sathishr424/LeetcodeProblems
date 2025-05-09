# Last updated: 10/5/2025, 3:44:17 am
mod = 10**9 + 7

fact = [0] * 81
fact[0] = 1
inverses = [1] * 81

def inverse(num):
    return pow(num, mod-2, mod)

for i in range(1, 81):
    fact[i] = i * fact[i-1] % mod
    inverses[i] = inverse(fact[i])

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)

        total = 0
        freq = [0] * 10

        for i in range(n):
            num_ = int(num[i])
            total += num_
            freq[num_] += 1
        
        if total % 2: return 0

        half = n // 2
        combined = fact[half] * fact[n-half] % mod
        
        @cache
        def dfs(index, need, cnt):
            if index == 10:
                if need == 0 and cnt == half:
                    return combined
                return 0
            
            if index == 10: return 0

            ans = 0
            r = freq[index]
            
            for l in range(freq[index] + 1):
                if need < 0 or cnt > half: break
                curr = (dfs(index+1, need, cnt+l) * inverses[l] % mod) * inverses[r] % mod

                ans = (ans + curr) % mod
                r -= 1
                need -= index
            
            return ans
        
        return dfs(0, total // 2, 0)